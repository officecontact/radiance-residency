import re

# FAQ sections HTML for packing page
packing_faq_section = '''        <!-- ======================== FAQ SECTION ======================== -->
        <section class="faq section" id="faq" aria-label="Frequently asked questions">
            <div class="container">
                <div class="section-header text-center">
                    <span class="section-badge" data-en="FAQs" data-hi="अक्सर पूछे जाने वाले प्रश्न">FAQs</span>
                    <h2 class="section-title" data-en="Hostel Packing <span>FAQs</span>" data-hi="हॉस्टल पैकिंग <span>प्रश्न</span>">Hostel Packing <span>FAQs</span></h2>
                </div>
                <div class="faq-list">
                    <!-- FAQ 1 -->
                    <details class="faq-item">
                        <summary class="faq-question">
                            <span data-en="What are the most essential items to pack for hostel life in India?" data-hi="भारत में हॉस्टल जीवन के लिए पैक करने के लिए सबसे आवश्यक वस्तुएं कौन सी हैं?">What are the most essential items to pack for hostel life in India?</span>
                            <i class="fas fa-chevron-down faq-icon" aria-hidden="true"></i>
                        </summary>
                        <div class="faq-answer">
                            <p>The most essential items include ID proof, college admission letter, prescribed medicines, basic toiletries, 5-7 sets of clothes (mix of regular wear and formal wear), undergarments, socks, comfortable shoes, formal shoes, study materials, laptop/tablet, phone charger, power bank, and important documents like birth certificate and vaccination records.</p>
                        </div>
                    </details>

                    <!-- FAQ 2 -->
                    <details class="faq-item">
                        <summary class="faq-question">
                            <span data-en="Can I buy things after reaching the hostel if I forget something?" data-hi="अगर मैं कुछ भूल जाऊं तो क्या मैं हॉस्टल पहुंचने के बाद चीजें खरीद सकता हूं?">Can I buy things after reaching the hostel if I forget something?</span>
                            <i class="fas fa-chevron-down faq-icon" aria-hidden="true"></i>
                        </summary>
                        <div class="faq-answer">
                            <p>Yes, absolutely! Indore has plenty of shopping markets and stores. However, you may end up paying premium prices for urgent purchases. It's better to pack thoughtfully to avoid last-minute expenses. Radiance Residency is conveniently located near Rau market where you can find most daily essentials.</p>
                        </div>
                    </details>

                    <!-- FAQ 3 -->
                    <details class="faq-item">
                        <summary class="faq-question">
                            <span data-en="What items should I NOT pack for hostel?" data-hi="मुझे हॉस्टल के लिए क्या नहीं पैक करना चाहिए?">What items should I NOT pack for hostel?</span>
                            <i class="fas fa-chevron-down faq-icon" aria-hidden="true"></i>
                        </summary>
                        <div class="faq-answer">
                            <p>Avoid packing large appliances like kettles, heaters, or cooking equipment as most hostels don't allow them for safety reasons. Also skip heavy footwear you won't use, excessive formal wear, and valuable jewelry. Check your hostel's specific rules before packing, as policies vary.</p>
                        </div>
                    </details>

                    <!-- FAQ 4 -->
                    <details class="faq-item">
                        <summary class="faq-question">
                            <span data-en="Where can I buy hostel essentials in Indore?" data-hi="मैं इंदौर में हॉस्टल की आवश्यक चीजें कहां खरीद सकता हूं?">Where can I buy hostel essentials in Indore?</span>
                            <i class="fas fa-chevron-down faq-icon" aria-hidden="true"></i>
                        </summary>
                        <div class="faq-answer">
                            <p>Indore has excellent shopping options. Vijay Nagar Market (near Medicaps) has clothing and accessories. Sarafa Bazaar and 56 Dukan have general merchandise. For electronics, visit CH Road or Palasia. Radiance Residency is walking distance from Rau market with all essentials nearby.</p>
                        </div>
                    </details>

                    <!-- FAQ 5 -->
                    <details class="faq-item">
                        <summary class="faq-question">
                            <span data-en="What if I forget to pack something important?" data-hi="अगर मैं कुछ महत्वपूर्ण पैक करना भूल जाऊं तो क्या होगा?">What if I forget to pack something important?</span>
                            <i class="fas fa-chevron-down faq-icon" aria-hidden="true"></i>
                        </summary>
                        <div class="faq-answer">
                            <p>Don't worry! Most items can be purchased in Indore. Major cities near Indore also have online shopping with quick delivery. If you're staying at Radiance Residency, our staff can help guide you to nearby shops for any missing items.</p>
                        </div>
                    </details>
                </div>
            </div>
        </section>
'''

# FAQ sections HTML for colleges page
colleges_faq_section = '''        <!-- ======================== FAQ SECTION ======================== -->
        <section class="faq section" id="faq" aria-label="Frequently asked questions">
            <div class="container">
                <div class="section-header text-center">
                    <span class="section-badge" data-en="FAQs" data-hi="अक्सर पूछे जाने वाले प्रश्न">FAQs</span>
                    <h2 class="section-title" data-en="Hostels Near Top <span>Colleges</span>" data-hi="शीर्ष <span>कॉलेजों</span> के पास हॉस्टल">Hostels Near Top <span>Colleges</span></h2>
                </div>
                <div class="faq-list">
                    <!-- FAQ 1 -->
                    <details class="faq-item">
                        <summary class="faq-question">
                            <span data-en="What is the best hostel near top colleges in Rau, Indore?" data-hi="राउ, इंदौर में शीर्ष कॉलेजों के पास सबसे अच्छा हॉस्टल कौन सा है?">What is the best hostel near top colleges in Rau, Indore?</span>
                            <i class="fas fa-chevron-down faq-icon" aria-hidden="true"></i>
                        </summary>
                        <div class="faq-answer">
                            <p>Radiance Residency is conveniently located in Pigdamber, Rau, just a 2-minute walk from Medicaps University. It's also ideally positioned near SD Bansal College, IPS Academy, IIST, and IIM Indore. With premium amenities, home-cooked meals, 24/7 CCTV security, and affordable pricing starting at ₹7,000/month, it's the best choice for students.</p>
                        </div>
                    </details>

                    <!-- FAQ 2 -->
                    <details class="faq-item">
                        <summary class="faq-question">
                            <span data-en="How far is Radiance Residency from major colleges in Rau?" data-hi="राउ के प्रमुख कॉलेजों से रेडियंस रेसीडेंसी कितनी दूर है?">How far is Radiance Residency from major colleges in Rau?</span>
                            <i class="fas fa-chevron-down faq-icon" aria-hidden="true"></i>
                        </summary>
                        <div class="faq-answer">
                            <p>Radiance Residency is located within walking distance of most top colleges: Medicaps University (2 minutes walk), SD Bansal College (10 minutes walk), IPS Academy (15 minutes walk by auto), IIST (20 minutes walk), and IIM Indore (30 minutes by auto). All are easily accessible for daily commute.</p>
                        </div>
                    </details>

                    <!-- FAQ 3 -->
                    <details class="faq-item">
                        <summary class="faq-question">
                            <span data-en="Do hostels provide transportation to colleges?" data-hi="क्या हॉस्टल कॉलेजों को परिवहन सेवा प्रदान करते हैं?">Do hostels provide transportation to colleges?</span>
                            <i class="fas fa-chevron-down faq-icon" aria-hidden="true"></i>
                        </summary>
                        <div class="faq-answer">
                            <p>Radiance Residency doesn't provide a shuttle, but its location near Medicaps makes walking convenient. For other colleges, students use auto-rickshaws or bikes. Indore has affordable local transport. Most students prefer staying close to campus like at Radiance Residency to minimize commute time.</p>
                        </div>
                    </details>

                    <!-- FAQ 4 -->
                    <details class="faq-item">
                        <summary class="faq-question">
                            <span data-en="What is the average cost of living near colleges in Rau, Indore?" data-hi="राउ, इंदौर के कॉलेजों के पास रहने की औसत लागत क्या है?">What is the average cost of living near colleges in Rau, Indore?</span>
                            <i class="fas fa-chevron-down faq-icon" aria-hidden="true"></i>
                        </summary>
                        <div class="faq-answer">
                            <p>At Radiance Residency, the total monthly cost is ₹7,000-₹9,000 (rent including all amenities and meals). Additional expenses for food outside, entertainment, and transport typically add ₹2,000-₹4,000/month, making the total ₹9,000-₹13,000 for comfortable college life.</p>
                        </div>
                    </details>

                    <!-- FAQ 5 -->
                    <details class="faq-item">
                        <summary class="faq-question">
                            <span data-en="Are there girls' hostels near these colleges?" data-hi="क्या इन कॉलेजों के पास लड़कियों के हॉस्टल हैं?">Are there girls' hostels near these colleges?</span>
                            <i class="fas fa-chevron-down faq-icon" aria-hidden="true"></i>
                        </summary>
                        <div class="faq-answer">
                            <p>Most colleges in Rau have their own girls' hostels. Radiance Residency is exclusively for boys, but the area has several girls' hostels nearby. We recommend checking directly with your college for girls' hostel options or contacting us for nearby recommendations.</p>
                        </div>
                    </details>
                </div>
            </div>
        </section>
'''

def add_faq_section_to_page(filepath, faq_html):
    """Add FAQ section before footer"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find footer comment and insert FAQ section before it
    footer_marker = '    <!-- ======================== FOOTER ======================== -->'
    if footer_marker in content:
        content = content.replace(footer_marker, faq_html + '\n' + footer_marker)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"[OK] Added FAQ section to {filepath}")
        return True
    else:
        print(f"[ERROR] Could not find footer marker in {filepath}")
        return False

# Process files
print("Adding visible FAQ sections to blog pages...\n")

if add_faq_section_to_page('blog/things-to-pack-for-hostel-life-india.html', packing_faq_section):
    print("Added packing list FAQ section")

print()

if add_faq_section_to_page('blog/top-colleges-in-rau-indore.html', colleges_faq_section):
    print("Added colleges guide FAQ section")

print("\nDone!")
