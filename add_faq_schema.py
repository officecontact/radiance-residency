import re

# FAQ data for packing list page
packing_faqs = [
    {
        "question": "What are the most essential items to pack for hostel life in India?",
        "answer": "The most essential items include ID proof, college admission letter, prescribed medicines, basic toiletries, 5-7 sets of clothes (mix of regular wear and formal wear), undergarments, socks, comfortable shoes, formal shoes, study materials, laptop/tablet, phone charger, power bank, and important documents like birth certificate and vaccination records."
    },
    {
        "question": "Can I buy things after reaching the hostel if I forget something?",
        "answer": "Yes, absolutely! Indore has plenty of shopping markets and stores. However, you may end up paying premium prices for urgent purchases. It's better to pack thoughtfully to avoid last-minute expenses. Radiance Residency is conveniently located near Rau market where you can find most daily essentials."
    },
    {
        "question": "What items should I NOT pack for hostel?",
        "answer": "Avoid packing large appliances like kettles, heaters, or cooking equipment as most hostels don't allow them for safety reasons. Also skip heavy footwear you won't use, excessive formal wear, and valuable jewelry. Check your hostel's specific rules before packing, as policies vary."
    },
    {
        "question": "Where can I buy hostel essentials in Indore?",
        "answer": "Indore has excellent shopping options. Vijay Nagar Market (near Medicaps) has clothing and accessories. Sarafa Bazaar and 56 Dukan have general merchandise. German Bakery area has cafes and food items. For electronics, visit CH Road or Palasia. Radiance Residency is walking distance from Rau market."
    },
    {
        "question": "What if I forget to pack something important?",
        "answer": "Don't worry! Most items can be purchased in Indore. Major cities near Indore also have online shopping with quick delivery. If you're staying at Radiance Residency, our staff can help guide you to nearby shops for any missing items."
    },
    {
        "question": "How much luggage can I bring to a hostel?",
        "answer": "Most hostels allow 1-2 large suitcases or bags. Radiance Residency provides storage space for extra luggage you don't need immediately. It's best to pack efficiently and avoid overloading on your first trip. You can always ask your hostel for specific luggage policies."
    },
    {
        "question": "Are there any restricted items in student hostels?",
        "answer": "Most hostels prohibit weapons, illegal substances, and cooking appliances for safety and security reasons. Some restrict large entertainment systems, pets, or excessive décor. Check your specific hostel's rules. Radiance Residency maintains comprehensive house rules available during booking."
    },
    {
        "question": "Should I pack different items for different seasons?",
        "answer": "Yes! Indore has distinct seasons. Summer (March-June) requires light clothing, sunscreen, and a hat. Monsoon (June-September) needs an umbrella and water-resistant shoes. Winter (November-February) requires sweaters and jackets. Pack versatile clothes and add seasonal items as needed."
    }
]

# FAQ data for colleges page
colleges_faqs = [
    {
        "question": "What is the best hostel near top colleges in Rau, Indore?",
        "answer": "Radiance Residency is conveniently located in Pigdamber, Rau, just a 2-minute walk from Medicaps University. It's also ideally positioned near SD Bansal College, IPS Academy, IIST, and IIM Indore. With premium amenities, home-cooked meals, 24/7 CCTV security, and affordable pricing starting at ₹7,000/month, it's the best choice for students."
    },
    {
        "question": "How far is Radiance Residency from major colleges in Rau?",
        "answer": "Radiance Residency is located within walking distance of most top colleges: Medicaps University (2 minutes walk), SD Bansal College (10 minutes walk), IPS Academy (15 minutes walk by auto), IIST (20 minutes walk), and IIM Indore (30 minutes by auto). All are easily accessible for daily commute."
    },
    {
        "question": "Do hostels provide transportation to colleges?",
        "answer": "Radiance Residency doesn't provide a shuttle, but its location near Medicaps makes walking convenient. For other colleges, students use auto-rickshaws or bikes. Indore has affordable local transport. Most students prefer staying close to campus like at Radiance Residency to minimize commute time."
    },
    {
        "question": "What is the average cost of living near colleges in Rau, Indore?",
        "answer": "At Radiance Residency, the total monthly cost is ₹7,000-₹9,000 (rent including all amenities and meals). Additional expenses for food outside, entertainment, and transport typically add ₹2,000-₹4,000/month, making the total ₹9,000-₹13,000 for comfortable college life."
    },
    {
        "question": "Are there girls' hostels near these colleges?",
        "answer": "Most colleges in Rau have their own girls' hostels. Radiance Residency is exclusively for boys, but the area has several girls' hostels nearby. We recommend checking directly with your college for girls' hostel options or contacting us for nearby recommendations."
    },
    {
        "question": "Which college has the best overall reputation in Rau?",
        "answer": "Medicaps University and IPS Academy are among the most reputed institutions in Rau for engineering and management programs. They have strong placements, experienced faculty, and good campus facilities. Students from all these colleges trust Radiance Residency as their home away from home."
    }
]

def add_faq_to_head(filepath, faqs, page_type="packing"):
    """Add FAQ schema to HTML head before </head> tag"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Build FAQ schema
    faq_items = []
    for faq in faqs:
        faq_items.append(f'''            {{
                "@type": "Question",
                "name": "{faq['question']}",
                "acceptedAnswer": {{
                    "@type": "Answer",
                    "text": "{faq['answer']}"
                }}
            }}''')
    
    faq_schema = f'''    <!-- JSON-LD: FAQPage -->
    <script type="application/ld+json">
    {{
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
{','.join([f + '\n' for f in faq_items[:-1]])}
{faq_items[-1]}
        ]
    }}
    </script>
'''
    
    # Insert FAQ schema before </head>
    if '</head>' in content:
        content = content.replace('</head>', faq_schema + '</head>')
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"[OK] Added FAQ schema to {filepath} ({len(faqs)} FAQs)")
        return True
    else:
        print(f"[ERROR] Could not find </head> in {filepath}")
        return False

# Process files
print("Adding FAQ schema to blog pages...\n")

if add_faq_to_head('blog/things-to-pack-for-hostel-life-india.html', packing_faqs, "packing"):
    print("Added packing list FAQs")

print()

if add_faq_to_head('blog/top-colleges-in-rau-indore.html', colleges_faqs, "colleges"):
    print("Added colleges guide FAQs")

print("\nDone!")
