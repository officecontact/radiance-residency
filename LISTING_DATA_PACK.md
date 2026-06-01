# Radiance Residency — Listing Data Pack

**Purpose:** copy-paste-ready data for creating clean listings on Bing Places, Apple Business Connect, OpenStreetMap, Trustpilot, and a fresh Google Business Profile. Every value below is pulled from the live website schema so your NAP stays identical everywhere — that consistency is what rebuilds the entity signal that drives both Google and AI (ChatGPT/Perplexity) rankings.

Generated 2026-06-01. Source of truth: `index.html` JSON-LD.

---

## 0. MASTER NAP — must be byte-identical on every platform

> ⚠️ **The single most important rule.** Google and AI engines match your business across sources by Name + Address + Phone. One inconsistent field weakens the link. Pick ONE value for each and never vary it.

| Field | Value |
|---|---|
| **Business name** | Radiance Residency |
| **Street** | In front of Medicaps University, Pigdamber |
| **Locality** | Rau, Indore |
| **Region** | Madhya Pradesh |
| **Postal code** | 453331 |
| **Country** | India |
| **Full address (one line)** | In front of Medicaps University, Pigdamber, Rau, Indore, Madhya Pradesh 453331, India |
| **Phone** | +91 8770445161 |
| **Email** | info@radianceresidency.com |
| **Website** | https://radianceresidency.com |
| **Latitude** | 22.6234773 |
| **Longitude** | 75.8010012 |

### ⚠️ Phone-number decision (read before Google)
The fresh-GBP plan in your notes called for a **new SIM** number to avoid matching the old "Smile Guru" listing. But for the **entity signal**, the phone should be the *same* number that's on your website (`+91 8770445161`). You can't have it both ways:
- **Use 8770445161 everywhere** → strongest entity consistency for rankings, but the new Google listing more easily links to the old location/Smile Guru.
- **Use a new SIM on Google only** → cleaner separation from Smile Guru, but the website ↔ Google phone won't match, weakening the signal.

**My recommendation:** use `+91 8770445161` everywhere (Bing/Apple/OSM/Trustpilot **and** the new Google listing). Consistency matters more than separation, and the Smile Guru listing fades on its own. Decide this before you start Google.

---

## 1. CATEGORIES (each platform names them differently)

| Platform | Primary category | Secondary categories |
|---|---|---|
| **Google Business Profile** | Student dormitory | Hostel, Boarding house, Dormitory, Student housing center |
| **Bing Places** | Student Housing | Hostel, Dormitory |
| **Apple Business Connect** | Hotels & Travel → Hostel | Lodging |
| **OpenStreetMap** | `tourism=hostel` | `building=dormitory` (see §6) |
| **Trustpilot** | Hostel / Student Accommodation | Property Rental |

---

## 2. DESCRIPTIONS (three lengths — use the one each form allows)

**Short (≤100 chars):**
> Boys hostel & PG in Rau, Indore — AC/non-AC rooms, home-style meals, Wi-Fi, 24/7 CCTV security.

**Medium (~250 chars — Bing, Apple):**
> Radiance Residency is a boys hostel and PG in Pigdamber, Rau, Indore, directly in front of Medicaps University. Furnished AC and non-AC rooms with home-style meals, high-speed Wi-Fi, 24/7 CCTV security, RO drinking water, daily housekeeping, and study areas.

**Long (~750 chars — Google, Trustpilot, OSM `description`):**
> Radiance Residency is a premium boys hostel and paying-guest (PG) accommodation in Pigdamber, Rau, Indore — located directly in front of Medicaps University and minutes from IPS Academy, SD Bansal College, and IIST. We offer 64 furnished AC and non-AC rooms with home-style vegetarian meals, high-speed Wi-Fi, 24/7 CCTV security, RO-purified drinking water, daily housekeeping, laundry service, quiet study areas, a rooftop lounge, power backup, and free tiffin delivery to campus. Ideal for engineering and management students as well as working professionals near the Pithampur industrial area. English and Hindi spoken. Flexible check-in. Contact us on WhatsApp for a room tour.

---

## 3. HOURS

Office / front-desk / reception hours (residence access is 24/7 — students live on-site):

| Day | Hours |
|---|---|
| Monday–Sunday | 9:00 AM – 10:30 PM |

> Use **09:00–22:30, all 7 days** on every platform (this matches the Google Business Profile). The 10:30 PM close aligns with the hostel gate-closing time in the rules. Keep these hours identical across all listings.

---

## 4. ATTRIBUTES / AMENITIES (tick these where the platform offers them)

Free Wi-Fi · 24/7 CCTV security · Air conditioning · Home-style meals · RO purified drinking water · Parking · Daily housekeeping · Laundry service · Study areas · Private bathrooms · Rooftop lounge · Free tiffin delivery to campus · Power backup · Hot water · On-campus mandir · Entertainment zone · 24–48 hr issue resolution

Also set: **Identifies as / serves** — students; **Gender** — boys/men's accommodation; **Languages** — English, Hindi; **Price range** — ₹9,000+/month (INR); **Payments** — Cash, UPI, Bank transfer.

---

## 5. PHOTO CHECKLIST (upload the same set to each; 10+ recommended)

- [ ] Building exterior / entrance (with signage if possible)
- [ ] AC room — wide
- [ ] Non-AC room — wide
- [ ] Bathroom (private)
- [ ] Dining area + a home-style meal plate
- [ ] Study area / desk
- [ ] Rooftop lounge
- [ ] CCTV / security desk
- [ ] Common / entertainment zone
- [ ] Logo (square, for profile) — `favicon.svg` on site, or a PNG export

> Use **real, consistent photos** across platforms — matching imagery reinforces it's the same verified entity. Avoid stock photos.

---

## 6. PLATFORM-BY-PLATFORM

### 🟦 Bing Places — *highest priority (feeds ChatGPT Search + Copilot)*
- URL: https://www.bingplaces.com → "Add a business" (single location, free)
- Fill: Master NAP + categories (§1) + medium description + hours + amenities + photos.
- **Verification:** phone or email (usually instant/fast). Use the master phone/email so it matches.
- After live, copy your Bing Places URL and send it to me.

### 🍎 Apple Business Connect
- URL: https://businessconnect.apple.com → sign in with an Apple ID → "Add a business."
- Apple often shows the place already exists from map data — **claim** it rather than duplicate.
- Fill: Master NAP + category (§1) + medium description + hours + photos.
- **Verification:** phone call/text, or document upload. No review system here, so it's attack-proof.
- Send me the Apple Maps place URL when live.

### 🗺️ OpenStreetMap — *I can help push this one (open API)*
- Easiest: https://www.openstreetmap.org → create account → search the address → **Edit** (iD editor) → add a Point → paste the tags below.
- Place the point at **lat 22.6234773, lon 75.8010012**.

```
tourism = hostel
name = Radiance Residency
operator = Radiance Residency
description = Boys hostel & PG in Rau, Indore, in front of Medicaps University. AC/non-AC rooms, meals, Wi-Fi, 24/7 CCTV.
addr:street = In front of Medicaps University, Pigdamber
addr:city = Rau, Indore
addr:state = Madhya Pradesh
addr:postcode = 453331
addr:country = IN
phone = +918770445161
contact:email = info@radianceresidency.com
website = https://radianceresidency.com
internet_access = wlan
internet_access:fee = no
building = dormitory
wikidata = Q139378489
```
> Note: OSM has no exact "student PG" tag; `tourism=hostel` is the closest renderable one and is what Apple Maps / DuckDuckGo / Mapbox read. The `wikidata=Q139378489` tag is gold — it directly links your OSM node to your verified Wikidata entity.
>
> **If you want me to push this via the OSM API** instead of editing by hand, give me an OSM account OAuth token and I'll create the node. (The web editor is honestly just as fast for one node.)

### ⭐ Trustpilot — *heavily scraped by AI training/answer pipelines*
- URL: https://business.trustpilot.com → claim/create the profile for `radianceresidency.com`.
- Domain verification (DNS TXT or meta tag) — **I can add the verification record to the site for you** once you start; just send me the token.
- Then invite real students by email/WhatsApp to leave reviews. No bad reviews exist here yet, so this is clean ground.

### 🔴 Google Business Profile — *the only thing that moves GOOGLE rankings*
- URL: https://business.google.com → "Add your business."
- ⚠️ **Merge risk (important):** your real location already hosts the dormant "Smile Guru" listing. A new listing at the same GPS may **merge into it** (dragging back the 1.9★ reviews) or get flagged as a duplicate. Before creating, open Google Maps at your address and check what's there.
  - If you proceed, **verify by phone/video** (instant) rather than postcard, and use the master NAP.
  - If it merges with Smile Guru, the real fix is disputing the fake reviews on that Place ID, not a second listing.
- Send me the new Place ID / share URL **only once it's clean and verified** — I'll re-link it then.

---

## 7. WHAT I DO WHEN EACH GOES LIVE

Ping me with **"<platform> done, URL: ..."** and I will (per your SEO-sync rule):
1. Add the URL to the `sameAs` cluster across all 10 schema files (index, reviews, about, faq, safety, testimonials, photos, calculator, find-your-room, api/info.json).
2. Update `llms.txt` + `llms-full.txt` Verified Listings.
3. Add a platform card to `/reviews.html`.
4. Cross-link it in Wikidata Q139378489.
5. Submit changed pages via Bing IndexNow + deploy.

A **multi-map sameAs cluster (Bing + Apple + OSM + Trustpilot + the new Google Place)** is a *stronger* entity anchor than the single Google link you had before — and none of it points at the bad reviews.

---

**Suggested order:** Bing → OSM → Apple → Trustpilot → (Google last, after checking the Smile Guru merge situation).
