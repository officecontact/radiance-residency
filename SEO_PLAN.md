# SEO_PLAN — radianceresidency.com

**Generated:** 2026-04-15 from TradeForge (GSC + DataForSEO + Moz + PageSpeed + onpage audit).

Open this folder in Claude Code and say: **"Read SEO_PLAN.md and implement Week 1"**.

---

## Week 1 — Mechanical fixes (17 pages need title/meta trimming)

### 1. `title_too_long` (17 pages) — trim every `<title>` to ≤60 chars
All blog posts, homepage, `amenities.html`, `contact.html`, `rooms.html`, `index.html`, the `hostel-near-*.html` landing pages. Pattern: `{Primary keyword} | Radiance Residency` (drop decorative tails).

### 2. `meta_too_long` (20 pages) — rewrite meta to ≤155 chars
Same pages. Template for landing: *"Premium student hostel near {college} in Indore. AC rooms, meals, Wi-Fi, security. Book a tour today."* (~115 chars, room for extras.)

---

## Week 2 — BIG CONTENT WIN (GSC data — ordered by impact)

**This is the most valuable section.** You have 15+ queries on page 2–4 with zero clicks. Push them up.

| Query | Current pos | Impressions | Action |
|---|---|---|---|
| student hostel in indore | 14.2 | 50 | Optimize `index.html` H1 + FAQ. Add `LocalBusiness` schema. |
| radiance residency | 7.1 | 48 | Brand query — add Organization schema, logo, contact. Target #1. |
| pg near medicaps university indore | 8.2 | 35 | Dedicated landing `/pg-near-medicaps-university.html` |
| hostel packing list for girl students | 1.8 | 27 | Already #1-2! Add FAQPage schema, expand to 1500+ words. |
| hostel essentials | 33.2 | 25 | Consolidated guide `/blog/hostel-essentials-complete-guide.html` |
| pg near ips academy indore | 6.6 | 24 | Dedicated landing |
| hostel packing list for students | 17.3 | 21 | Merge with girl-students post, internal link to product essentials |
| hostel requirements list | 31.5 | 20 | Combine into hostel essentials pillar page |
| best hostels in indore | 10.6 | 20 | Homepage H1 + listicle content + Review schema |
| hostel near ips academy indore | 6.7 | 19 | Dedicated landing |
| checklist for hostel students | 17.1 | 18 | Same pillar page, anchor link `#checklist` |
| essential things for hostel | 32.5 | 18 | Same pillar page |
| hostel needs list | 36.2 | 18 | Same pillar page |
| list of things required in hostel | 29.9 | 18 | Same pillar page |
| medicaps university hostel | 3.9 | 14 | Push to #1 with dedicated landing + photos |

**Content pattern = pillar + spokes:**
- **Pillar:** `/blog/ultimate-hostel-essentials-guide.html` — 2000 words, 15 H2s covering packing/requirements/checklist/essentials. Targets ~8 GSC queries with one page.
- **Spoke landings:** `/pg-near-medicaps-university.html`, `/pg-near-ips-academy.html`, `/hostel-near-iim-indore.html` (already exist — verify content is unique + ≥800 words each).

### Schema to add site-wide
```html
<script type="application/ld+json">
{"@context":"https://schema.org","@type":"LodgingBusiness",
 "name":"Radiance Residency",
 "address":{"@type":"PostalAddress","addressLocality":"Indore","addressRegion":"MP","addressCountry":"IN"},
 "telephone":"{phone}",
 "priceRange":"₹₹",
 "amenityFeature":[{"@type":"LocationFeatureSpecification","name":"AC"},{"@type":"LocationFeatureSpecification","name":"WiFi"},{"@type":"LocationFeatureSpecification","name":"Meals"},{"@type":"LocationFeatureSpecification","name":"24/7 Security"}]}
</script>
```
Add `FAQPage` schema on top blog posts (5 Q&A each) to unlock rich results.

---

## Week 3 — Local SEO
- **Google Business Profile**: ensure verified, photos, Q&A, posts (tradeforge parking_lot has instructions).
- Backlinks from Indore directories, college forums, student-accommodation listings.

---

## Data sources
GSC (the star here — drives the Week 2 queue), DataForSEO, Moz, PageSpeed, Bing, onpage crawler, SERP features.
