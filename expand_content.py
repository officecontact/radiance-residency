import re

# Content expansions for each page

index_html_why_choose = '''        <!-- ======================== WHY CHOOSE RADIANCE SECTION ======================== -->
        <section class="why-choose section" id="why-choose" aria-label="Why choose Radiance Residency">
            <div class="container">
                <div class="section-header text-center">
                    <span class="section-badge" data-en="Why Choose Us" data-hi="हमें क्यों चुनें">Why Choose Us</span>
                    <h2 class="section-title" data-en="Why Students Trust Radiance Residency" data-hi="छात्र रेडियंस रेसीडेंसी पर क्यों भरोसा करते हैं">Why Students Trust Radiance Residency</h2>
                </div>
                <div class="why-choose-grid" style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 2rem; margin-top: 3rem;">
                    <div class="why-choose-card" style="padding: 2rem; background: #f8f9ff; border-radius: 12px; border-left: 4px solid #6366f1;">
                        <h3 style="font-size: 1.25rem; margin-bottom: 1rem; color: #1f2937;">Unbeatable Location</h3>
                        <p>Located just 2 minutes from Medicaps University, we eliminate commute stress. Many students save 45+ minutes daily compared to hostels in other areas. This advantage extends to other colleges — SD Bansal (10 min), IPS Academy (15 min), and IIST (20 min) are all within easy reach. The location advantage means more sleep, more study time, and better academic performance.</p>
                    </div>
                    <div class="why-choose-card" style="padding: 2rem; background: #f8f9ff; border-radius: 12px; border-left: 4px solid #6366f1;">
                        <h3 style="font-size: 1.25rem; margin-bottom: 1rem; color: #1f2937;">Experienced Management</h3>
                        <p>With 5+ years of experience managing 64+ beds and 112+ students, our team understands student needs better than anyone. We've learned what works — from meal preferences to study schedules to emergency response times. This experience translates into 24-48 hour issue resolution and preventive maintenance that stops problems before they start.</p>
                    </div>
                    <div class="why-choose-card" style="padding: 2rem; background: #f8f9ff; border-radius: 12px; border-left: 4px solid #6366f1;">
                        <h3 style="font-size: 1.25rem; margin-bottom: 1rem; color: #1f2937;">Home-Style Culture</h3>
                        <p>Unlike commercial hostels that feel transactional, Radiance Residency is built on a family culture. Our staff knows every student by name. Regular community events, shared meals, and mentorship from senior students create bonds that last beyond college. Many students say it's their second home — that feeling can't be manufactured, only earned through genuine care and attention.</p>
                    </div>
                    <div class="why-choose-card" style="padding: 2rem; background: #f8f9ff; border-radius: 12px; border-left: 4px solid #6366f1;">
                        <h3 style="font-size: 1.25rem; margin-bottom: 1rem; color: #1f2937;">Transparent Pricing</h3>
                        <p>No hidden fees. No surprises. At ₹7,000-₹9,000/month with all amenities and meals included, we're actually more affordable than independent flats (₹8,000-₹12,000 rent alone). Our pricing advantage + location advantage + community value = best ROI for student accommodation in Rau, Indore.</p>
                    </div>
                </div>
            </div>
        </section>
'''

medicaps_expansion = '''        <!-- ======================== WHY MEDICAPS STUDENTS CHOOSE US ======================== -->
        <section class="medicaps-advantage section section-light" id="medicaps-advantage" aria-label="Why Medicaps students choose Radiance">
            <div class="container">
                <div class="section-header text-center">
                    <h2 class="section-title" data-en="Perfect for Medicaps Students" data-hi="मेडीकैप्स के छात्रों के लिए सही">Perfect for Medicaps Students</h2>
                </div>
                <div style="max-width: 800px; margin: 2rem auto; line-height: 1.8; color: #4b5563; font-size: 1.05rem;">
                    <p><strong>Medicaps University students choose Radiance Residency for one simple reason: proximity + support.</strong> Being just 2 minutes from campus isn't just a convenience—it changes your entire college experience. When classes end at 1 PM, you're back in your room by 1:10. When you have lab submissions or projects due, you can work late and still eat on time. When you need something from home (notes, documents, clothes), parents visiting campus can stop by the hostel in minutes.</p>

                    <p><strong>Beyond location, we understand Medicaps' academic culture.</strong> We host study groups in our common areas. Our Wi-Fi speed (50+ Mbps) handles online submissions and research without lag. We provide flexible meal timings for students with irregular class schedules. During exam season, our staff ensures quiet hours and provides extra support.</p>

                    <p><strong>And we're not just a hostel—we're part of the Medicaps community.</strong> Our residents represent different departments (Engineering, Management, Commerce) and years (1st to Final), creating a peer network that helps academics and career growth. Many of our residents have landed internships and jobs through hostel connections.</p>
                </div>
            </div>
        </section>
'''

packing_seasonal = '''        <!-- ======================== SEASONAL PACKING GUIDE ======================== -->
        <section class="packing-seasonal section" id="seasonal-packing" aria-label="Seasonal packing guide">
            <div class="container">
                <div class="section-header text-center">
                    <h2 class="section-title" data-en="Packing Guide by Season" data-hi="मौसम के अनुसार पैकिंग गाइड">Packing Guide by Season</h2>
                </div>
                <div style="max-width: 900px; margin: 2rem auto;">
                    <div style="margin-bottom: 2rem; padding: 1.5rem; background: #fff3cd; border-radius: 8px; border-left: 4px solid #ffc107;">
                        <h3 style="color: #b8860b; margin-bottom: 0.5rem;">Summer (March - June): Light & Breathable</h3>
                        <p>Indore summers are hot and dry (40-45C). Pack 8-10 light cotton t-shirts, 3-4 shorts, 1-2 lightweight pants, light summer dresses, and sleeveless tops. Don't forget: sunscreen (SPF 50+), sunglasses, a wide-brimmed hat or cap, light scarf for AC rooms (temperature shock is real), and moisture-wicking socks. A light sleeping mat or cotton sheet—some hostels provide heavy blankets unsuitable for summer. Avoid: heavy jeans, formal wear (unless essential), thick sweaters.</p>
                    </div>

                    <div style="margin-bottom: 2rem; padding: 1.5rem; background: #cff0fc; border-radius: 8px; border-left: 4px solid #0dcaf0;">
                        <h3 style="color: #0c5460; margin-bottom: 0.5rem;">Monsoon (June - September): Waterproof & Extra Care</h3>
                        <p>Indore receives moderate rainfall (around 700mm annually). Pack a good quality waterproof jacket or poncho, water-resistant shoes or sandals, 1-2 pairs of water-absorbent socks, light sweaters (mornings get cool), 6-8 light clothes that dry quickly. Essential: waterproof bag for electronics, portable umbrella (compact design), moisture-absorbent shoes or slippers for hostel rooms. The monsoon makes rooms damp—add a small dehumidifier or silica gel packets. Avoid: light colored clothes (they stain easily with dirt), open canvas shoes.</p>
                    </div>

                    <div style="padding: 1.5rem; background: #d1e7dd; border-radius: 8px; border-left: 4px solid #198754;">
                        <h3 style="color: #0f5132; margin-bottom: 0.5rem;">Winter (November - February): Layering is Key</h3>
                        <p>Winters in Indore are mild (8-25C) but require proper layering. Pack 6-8 regular t-shirts, 3-4 sweaters or hoodies (avoid one-size-fits-all; layering works better), 2-3 light jackets, full-length pajamas, 1 formal jacket, and thermal wear (if you're cold-sensitive). Don't pack: heavy winter coats (not needed, wasted space). Instead focus on: moisture-wicking inner layers, warm socks, a light scarf, and a blanket from home if your hostel allows (most do). Winter dryness can affect skin—pack a good moisturizer and lip balm.</p>
                    </div>
                </div>
            </div>
        </section>
'''

colleges_advantage = '''        <!-- ======================== RADIANCE ADVANTAGE FOR EACH COLLEGE ======================== -->
        <section class="colleges-advantage section section-light" id="college-advantage" aria-label="Radiance advantage for each college">
            <div class="container">
                <div class="section-header text-center">
                    <h2 class="section-title" data-en="Radiance Advantage for Your College" data-hi="आपके कॉलेज के लिए रेडियंस का फायदा">Radiance Advantage for Your College</h2>
                </div>
                <div style="max-width: 900px; margin: 2rem auto; line-height: 1.8; color: #4b5563; font-size: 1rem;">
                    <p><strong>Medicaps University (2 min walk):</strong> Zero commute. Study until midnight, sleep in, attend 9 AM classes without time pressure. Ideal for students with back-to-back labs or project submissions.</p>

                    <p><strong>SD Bansal College (10 min walk):</strong> Walking distance or quick auto. Our residents from SD Bansal appreciate the peaceful location—far from Indore's chaos but close enough for daily attendance. Great for architecture and design students who need to work late on projects.</p>

                    <p><strong>IPS Academy (15 min by auto):</strong> Affordable auto-share with other residents. IPS students benefit from our peer network—many seniors have cleared IPS entrance exams and can mentor juniors. We have a study group specifically for IPS CLAT/CAT preparation.</p>

                    <p><strong>IIST Indore (20 min walk):</strong> Close enough for daily commute without Uber costs. IIST students stay with us specifically for the cost advantage and community—hostel community greater than high-cost paying guest flats.</p>

                    <p><strong>IIM Indore (30 min auto):</strong> Not as close as Medicaps, but we have several IIM residents who chose us for the value proposition. The hostel supports all-nighters during IIM CAT prep season with 24-hour meal support and study-friendly environment.</p>

                    <p style="margin-top: 1.5rem; padding: 1rem; background: #f0f5ff; border-radius: 8px; border-left: 4px solid #6366f1;"><strong>Bottom line:</strong> No matter which Rau college you attend, Radiance Residency saves you 30-60 minutes daily in commute time. Over a 4-year college life, that's 500+ hours—equivalent to 60+ extra study days. Location matters more than you think.</p>
                </div>
            </div>
        </section>
'''

def insert_section(filepath, section_html, insertion_marker):
    """Insert section after a specific marker"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    if insertion_marker in content:
        content = content.replace(insertion_marker, insertion_marker + section_html)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print("[OK] Added section to {}".format(filepath))
        return True
    else:
        print("[ERROR] Could not find insertion marker in {}".format(filepath))
        return False

# Process files
print("Expanding content on target pages...\n")

# 1. index.html - Add after ABOUT section
if insert_section('index.html', index_html_why_choose, '        </section>\n\n        <!-- ======================== AMENITIES SECTION ======================== -->'):
    print("Added 'Why Choose Radiance' section to index.html")

# 2. hostel-near-medicaps-university.html
with open('hostel-near-medicaps-university.html', 'r', encoding='utf-8') as f:
    medicaps_content = f.read()
if '        <!-- ======================== FAQ SECTION ======================== -->' in medicaps_content:
    medicaps_content = medicaps_content.replace(
        '        <!-- ======================== FAQ SECTION ======================== -->',
        medicaps_expansion + '\n        <!-- ======================== FAQ SECTION ======================== -->'
    )
    with open('hostel-near-medicaps-university.html', 'w', encoding='utf-8') as f:
        f.write(medicaps_content)
    print("Added 'Why Medicaps' section to hostel-near-medicaps-university.html")

# 3. blog/things-to-pack-for-hostel-life-india.html
with open('blog/things-to-pack-for-hostel-life-india.html', 'r', encoding='utf-8') as f:
    packing_content = f.read()
if '        <!-- ======================== FAQ SECTION ======================== -->' in packing_content:
    packing_content = packing_content.replace(
        '        <!-- ======================== FAQ SECTION ======================== -->',
        packing_seasonal + '\n\n        <!-- ======================== FAQ SECTION ======================== -->'
    )
    with open('blog/things-to-pack-for-hostel-life-india.html', 'w', encoding='utf-8') as f:
        f.write(packing_content)
    print("Added 'Seasonal Packing Guide' to blog/things-to-pack-for-hostel-life-india.html")

# 4. blog/top-colleges-in-rau-indore.html
with open('blog/top-colleges-in-rau-indore.html', 'r', encoding='utf-8') as f:
    colleges_content = f.read()
if '        <!-- ======================== FAQ SECTION ======================== -->' in colleges_content:
    colleges_content = colleges_content.replace(
        '        <!-- ======================== FAQ SECTION ======================== -->',
        colleges_advantage + '\n\n        <!-- ======================== FAQ SECTION ======================== -->'
    )
    with open('blog/top-colleges-in-rau-indore.html', 'w', encoding='utf-8') as f:
        f.write(colleges_content)
    print("Added 'College Advantage' section to blog/top-colleges-in-rau-indore.html")

print("\nContent expansion complete!")
