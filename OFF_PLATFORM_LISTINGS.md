# Off-Platform Reputation Building — Action Guide

> **Purpose:** Build presence on 5 platforms outside Google's ecosystem. Each is independent of GBP (so the 1.9★ attack doesn't affect them). All copy-paste-ready below.
>
> **Total time:** ~75 minutes spread across all 5 platforms. Do them in any order.

---

## 🅰️ APPLE BUSINESS CONNECT (10 min) — iPhone users default to Apple Maps

**Why this matters:** ~25% of Indian smartphone users have iPhones. Apple Maps doesn't show Google reviews. Free listing.

**URL:** https://businessconnect.apple.com/

**Steps:**
1. Sign in with your Apple ID (create one with `info@radianceresidency.com` if needed)
2. Click **"Add place"**
3. Search "Radiance Residency" — if it appears in Apple Maps already, claim it. If not, click "Can't find your place" → add manually
4. Fill in the form with the data below
5. Verify via phone or postcard (postcard takes 1-2 weeks)

**Copy-paste data:**

| Field | Value |
|---|---|
| Business name | Radiance Residency |
| Category | Hostel (or "Student Accommodation") |
| Street address | In front of Medicaps University, Pigdamber |
| City | Rau, Indore |
| State | Madhya Pradesh |
| Postal code | 453331 |
| Country | India |
| Phone | +91-8770445161 |
| Email | info@radianceresidency.com |
| Website | https://radianceresidency.com |
| Latitude | 22.6234773 |
| Longitude | 75.8010012 |
| Hours | Open 24/7 |

**Description (copy-paste):**
> Premium boys hostel and PG accommodation directly in front of Medicaps University in Pigdamber, Rau, Indore. Founded 2022. 5 room categories from ₹9,000/month all-inclusive — meals, Wi-Fi, 24/7 CCTV security, air conditioning option, attached bathrooms, dedicated study areas. Convenient for students of Medicaps, SD Bansal, IPS Academy, IIST, and IIM Indore. Free daily lunch tiffin delivery to Medicaps campus.

**Photos to upload (6 minimum):** Use the same images that are on /photos page:
- outer-building-1.jpg
- building-day.webp
- room-furnished-double.webp
- dining-meals.jpg
- cctv-wifi.jpg
- big-parking-area.webp

---

## 🅱️ BING PLACES FOR BUSINESS (10 min) — ChatGPT search uses Bing's index

**Why this matters:** ChatGPT's web search, Microsoft Copilot, and Yahoo all use Bing's local index. **Radiance Residency is already verified on Bing Webmaster Tools** — Bing Places needs separate setup but uses the same Microsoft account.

**URL:** https://www.bingplaces.com/

**Steps:**
1. Sign in with the same Microsoft account that owns the Webmaster Tools account
2. Click **"New User?"** → **"Get Started"**
3. Search for your business — if not found, click "Add new business"
4. Fill the form with the data below
5. Verify via phone (you receive an OTP)

**Copy-paste data:** Same as Apple Business above.

**Categories to select:**
- Primary: **Hostel**
- Secondary: **Student Housing**, **Paying Guest Accommodation**

**Description (copy-paste):**
> The most premium boys hostel near Medicaps University in Pigdamber, Rau, Indore. Founded 2022. Located 2 minutes walk from the campus. 5 room categories from ₹9,000/month, all-inclusive (meals, Wi-Fi, 24/7 security, AC option, attached bathrooms). Verified on Wikidata Q139378489.

---

## 🌍 OPENSTREETMAP (15 min) — Foundation for Apple Maps, Mapbox, DuckDuckGo

**Why this matters:** OSM data powers Apple Maps, Mapbox, MapKit, DuckDuckGo, and many AI services. Claim once, benefit everywhere. **No review system on OSM — bulletproof signal.**

**URL:** https://www.openstreetmap.org/

**Steps:**
1. Sign up at https://www.openstreetmap.org/user/new (use `info@radianceresidency.com`)
2. Verify email → log in
3. Navigate to: https://www.openstreetmap.org/#map=19/22.6234773/75.8010012
4. Look for the building at the marked location. If it already exists as a footprint, click it. If not, click **"Edit"** (top-left)
5. In the iD editor: Click on the building polygon. If no polygon, draw one over the building.
6. Search for **"Hostel"** in the feature type search and select **Tourism → Hostel**
7. Fill the side panel fields:

**Copy-paste tags:**

| Field | Value |
|---|---|
| Name | Radiance Residency |
| Name (Hindi) | रेडियंस रेसीडेंसी |
| Address (housenumber) | In front of Medicaps University |
| Street | Pigdamber |
| City | Rau, Indore |
| Postcode | 453331 |
| Phone | +918770445161 |
| Email | info@radianceresidency.com |
| Website | https://radianceresidency.com |
| Operator | Radiance Residency |
| Capacity | 64 |
| Internet access | yes; wlan |
| Smoking | no |
| Wheelchair | yes |

Click **"All tags"** at the bottom and add these extra ones:
- `wikidata = Q139378489`
- `wikipedia = ` (leave blank unless Wikipedia article gets approved)
- `tourism = hostel`
- `male = yes` (boys-only)
- `start_date = 2022`

8. Click **Save** (top right) → enter changeset comment: "Added Radiance Residency hostel near Medicaps University"
9. Submit. Edits go live in OSM within hours; downstream services (Apple Maps, Mapbox) sync in 1-30 days.

---

## ⭐ TRUSTPILOT (15 min) — LLM crawlers scrape Trustpilot heavily

**Why this matters:** Trustpilot is heavily indexed by ChatGPT, Claude, and Perplexity. Even with zero reviews initially, the listing creates another `sameAs` link and earns a domain badge.

**URL:** https://business.trustpilot.com/signup

**Steps:**
1. Sign up with `info@radianceresidency.com`
2. Enter business domain: `radianceresidency.com`
3. Trustpilot will scan your domain for an existing free profile — if found, claim it
4. Pick the **Free plan** (don't upgrade — paid tiers aren't needed)
5. Complete profile with data below
6. Verify email
7. Verify domain via DNS TXT record (Trustpilot provides the value — add it via Cloudflare DNS dashboard or message me with the value and I'll add it)

**Copy-paste data:**

| Field | Value |
|---|---|
| Business name | Radiance Residency |
| Domain | radianceresidency.com |
| Category | Lodging > Hostel / Student Accommodation |
| Country | India |
| Phone | +91-8770445161 |
| Email | info@radianceresidency.com |

**Profile description (copy-paste):**
> Radiance Residency is a premium boys hostel and PG located directly opposite Medicaps University in Pigdamber, Rau, Indore. Founded in 2022, we have hosted 112+ students across 5 room categories starting at ₹9,000/month all-inclusive (meals, Wi-Fi, 24/7 security). Verified on Wikidata, Justdial, and MagicBricks.

---

## 📚 WIKIPEDIA ARTICLE (separate file: WIKIPEDIA_DRAFT.md)

**Why this matters:** Wikipedia articles get extremely high authority. Google's Knowledge Graph imports from Wikipedia. AI models train on Wikipedia.

**Notability bar is HIGH** — small businesses usually don't qualify. The article is drafted in `WIKIPEDIA_DRAFT.md`. ~30% chance of acceptance. Worth trying.

**Submission process:**
1. Create an account at https://en.wikipedia.org/wiki/Special:CreateAccount
2. Build edit history first: Edit 10 existing articles (typo fixes, small improvements) — Wikipedia auto-rejects new articles from accounts with no edit history
3. Wait 4+ days for autoconfirmed status
4. Use **Articles for Creation (AfC)** path: https://en.wikipedia.org/wiki/Wikipedia:Articles_for_creation
5. Copy the draft from `WIKIPEDIA_DRAFT.md`
6. Submit for review (1-2 month queue)

**Tips for higher acceptance:**
- Add 5+ independent reliable sources (news coverage, university accommodation lists, government registry)
- Avoid promotional language ("the most premium" type phrasing — Wikipedia hates this)
- Focus on facts: founding date, capacity, location, role in local education context
- Cite Justdial, MagicBricks listings as external sources

---

## 🎓 .EDU OUTREACH (separate file: EDU_OUTREACH_TEMPLATES.md)

**Why this matters:** When college websites list nearby accommodation, those backlinks are extremely high-authority. .edu/.ac.in domains pass huge link equity.

**Target colleges:**
1. Medicaps University (medicaps.ac.in)
2. IIST Indore (iist-indore.ac.in)
3. SD Bansal College
4. IPS Academy (ipsacademy.org)
5. IIM Indore (iimidr.ac.in)

**Process:**
1. Find each college's "Hostel/Accommodation" or "International Students" page
2. Find a contact email (usually accommodation officer, student affairs, or webmaster)
3. Send the email template (in `EDU_OUTREACH_TEMPLATES.md`)
4. Follow up after 1 week if no reply

Email templates in `EDU_OUTREACH_TEMPLATES.md`.

---

## 📊 TRACKING & FOLLOW-UP

After completing each listing, update this table:

| Platform | Status | Date submitted | Date verified | Notes |
|---|---|---|---|---|
| Apple Business Connect | ⏳ Pending | | | |
| Bing Places | ⏳ Pending | | | |
| OpenStreetMap | ⏳ Pending | | | |
| Trustpilot | ⏳ Pending | | | |
| Wikipedia AfC | ⏳ Pending | | | Hard — 30% acceptance |
| Medicaps email | ⏳ Pending | | | |
| IIST email | ⏳ Pending | | | |
| SD Bansal email | ⏳ Pending | | | |
| IPS Academy email | ⏳ Pending | | | |
| IIM Indore email | ⏳ Pending | | | |

---

## 📌 ONCE EACH LISTING IS LIVE

Tell me the live URL — I'll add it to:
1. `sameAs` cluster in JSON-LD schema across all pages
2. `/llms.txt` and `/llms-full.txt` (AI authority signal)
3. `/api/info.json` endpoints list
4. `/reviews.html` verification grid (visible platform card)
5. Wikidata Q139378489 (additional cross-references)

Each new listing compounds: more `sameAs` links = stronger Knowledge Graph entity authority = higher AI search citation rate.
