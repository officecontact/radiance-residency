"""Wikidata login + entity edit using bot creds from tradeforge .env.

Persists session via pickle so the email-2FA flow can span two CLI runs:
    1. python wd_login.py init    -> triggers email, saves session
    2. python wd_login.py verify <code>   -> submits code, saves logged-in session
    3. python wd_login.py edit    -> applies all Q139378489 enhancements
"""
import sys, os, json, pickle, requests
from pathlib import Path

ENV = Path(r"C:\Users\aagos\assets\tradeforge\.env")
SESSION_FILE = Path(os.environ["TEMP"]) / "wd_session.pkl"
API = "https://www.wikidata.org/w/api.php"
ENTITY = "Q139378489"

env = {}
for line in ENV.read_text().splitlines():
    if "=" in line and not line.lstrip().startswith("#"):
        k, v = line.split("=", 1)
        env[k.strip()] = v.strip()

USER = env["WIKIDATA_USERNAME"]
PASS = env["WIKIDATA_PASSWORD"]


def save(s):
    with open(SESSION_FILE, "wb") as f:
        pickle.dump(s.cookies, f)


def load():
    s = requests.Session()
    if SESSION_FILE.exists():
        with open(SESSION_FILE, "rb") as f:
            s.cookies = pickle.load(f)
    s.headers["User-Agent"] = "RadianceResidency-Bot/1.0 (info@radianceresidency.com)"
    return s


def cmd_init():
    s = requests.Session()
    s.headers["User-Agent"] = "RadianceResidency-Bot/1.0 (info@radianceresidency.com)"
    r = s.get(API, params={"action": "query", "meta": "tokens", "type": "login", "format": "json"})
    token = r.json()["query"]["tokens"]["logintoken"]
    r = s.post(API, data={
        "action": "clientlogin",
        "username": USER,
        "password": PASS,
        "logintoken": token,
        "loginreturnurl": "https://radianceresidency.com",
        "format": "json",
    })
    print(json.dumps(r.json(), indent=2))
    save(s)


def cmd_verify(code):
    s = load()
    r = s.get(API, params={"action": "query", "meta": "tokens", "type": "login", "format": "json"})
    token = r.json()["query"]["tokens"]["logintoken"]
    r = s.post(API, data={
        "action": "clientlogin",
        "logintoken": token,
        "logincontinue": "1",
        "token": code,
        "format": "json",
    })
    print(json.dumps(r.json(), indent=2))
    save(s)


def cmd_status():
    s = load()
    r = s.get(API, params={"action": "query", "meta": "userinfo", "format": "json"})
    print(json.dumps(r.json(), indent=2))


def cmd_edit():
    s = load()
    # Get CSRF
    r = s.get(API, params={"action": "query", "meta": "tokens", "format": "json"})
    csrf = r.json()["query"]["tokens"]["csrftoken"]
    if csrf == "+\\":
        print("ERROR: not logged in (got anonymous CSRF token). Run init+verify first.")
        return

    data = {
        "labels": {
            "hi": {"language": "hi", "value": "रेडियंस रेसिडेंसी"},
        },
        "descriptions": {
            "hi": {"language": "hi", "value": "रौ, इंदौर में मेडिकैप्स विश्वविद्यालय के पास लड़कों का छात्रावास"},
        },
        "aliases": {
            "en": [
                {"language": "en", "value": "Radiance Residency Hostel"},
                {"language": "en", "value": "Radiance Boys Hostel"},
                {"language": "en", "value": "Radiance PG Indore"},
                {"language": "en", "value": "Radiance Residency Rau"},
                {"language": "en", "value": "Radiance Residency Pigdamber"},
            ],
            "hi": [
                {"language": "hi", "value": "रेडियंस रेजीडेंसी"},
                {"language": "hi", "value": "रेडियंस होस्टल"},
            ],
        },
        "claims": [
            # P625 coordinates
            {
                "type": "statement",
                "mainsnak": {
                    "snaktype": "value", "property": "P625",
                    "datavalue": {
                        "value": {
                            "latitude": 22.6234773, "longitude": 75.8010012,
                            "precision": 0.0001,
                            "globe": "http://www.wikidata.org/entity/Q2"
                        },
                        "type": "globecoordinate"
                    }
                },
                "rank": "normal"
            },
            # P571 inception (2022)
            {
                "type": "statement",
                "mainsnak": {
                    "snaktype": "value", "property": "P571",
                    "datavalue": {
                        "value": {
                            "time": "+2022-00-00T00:00:00Z",
                            "timezone": 0, "before": 0, "after": 0,
                            "precision": 9,
                            "calendarmodel": "http://www.wikidata.org/entity/Q1985727"
                        },
                        "type": "time"
                    }
                },
                "rank": "normal"
            },
            # P1083 maximum capacity (64)
            {
                "type": "statement",
                "mainsnak": {
                    "snaktype": "value", "property": "P1083",
                    "datavalue": {
                        "value": {"amount": "+64", "unit": "1"},
                        "type": "quantity"
                    }
                },
                "rank": "normal"
            },
            # P281 postal code
            {
                "type": "statement",
                "mainsnak": {
                    "snaktype": "value", "property": "P281",
                    "datavalue": {"value": "453331", "type": "string"}
                },
                "rank": "normal"
            },
            # P6375 street address (monolingual text)
            {
                "type": "statement",
                "mainsnak": {
                    "snaktype": "value", "property": "P6375",
                    "datavalue": {
                        "value": {"text": "In front of Medicaps University, Pigdamber, Rau, Indore", "language": "en"},
                        "type": "monolingualtext"
                    }
                },
                "rank": "normal"
            },
            # P1329 phone
            {
                "type": "statement",
                "mainsnak": {
                    "snaktype": "value", "property": "P1329",
                    "datavalue": {"value": "+91-8770445161", "type": "string"}
                },
                "rank": "normal"
            },
            # P968 email
            {
                "type": "statement",
                "mainsnak": {
                    "snaktype": "value", "property": "P968",
                    "datavalue": {"value": "mailto:info@radianceresidency.com", "type": "string"}
                },
                "rank": "normal"
            },
            # P131 located in Madhya Pradesh (additional location refinement)
            {
                "type": "statement",
                "mainsnak": {
                    "snaktype": "value", "property": "P131",
                    "datavalue": {
                        "value": {"entity-type": "item", "numeric-id": 1184, "id": "Q1184"},
                        "type": "wikibase-entityid"
                    }
                },
                "rank": "normal"
            },
            # P407 language: English (Q1860)
            {
                "type": "statement",
                "mainsnak": {
                    "snaktype": "value", "property": "P407",
                    "datavalue": {
                        "value": {"entity-type": "item", "numeric-id": 1860, "id": "Q1860"},
                        "type": "wikibase-entityid"
                    }
                },
                "rank": "normal"
            },
            # P407 language: Hindi (Q1568)
            {
                "type": "statement",
                "mainsnak": {
                    "snaktype": "value", "property": "P407",
                    "datavalue": {
                        "value": {"entity-type": "item", "numeric-id": 1568, "id": "Q1568"},
                        "type": "wikibase-entityid"
                    }
                },
                "rank": "normal"
            },
        ],
    }

    r = s.post(API, data={
        "action": "wbeditentity",
        "id": ENTITY,
        "data": json.dumps(data),
        "token": csrf,
        "bot": "1",
        "summary": "Adding coordinates, founding date, capacity, address, contact, language, Hindi labels, and aliases for improved entity authority",
        "format": "json",
    })
    print(json.dumps(r.json(), indent=2))


if __name__ == "__main__":
    cmd = sys.argv[1] if len(sys.argv) > 1 else "status"
    if cmd == "init":
        cmd_init()
    elif cmd == "verify":
        cmd_verify(sys.argv[2])
    elif cmd == "edit":
        cmd_edit()
    elif cmd == "status":
        cmd_status()
    else:
        print("Usage: wd_login.py [init|verify <code>|edit|status]")
