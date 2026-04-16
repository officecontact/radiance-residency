import os
import re

# List of pages that need title fixes (from SEO_PLAN.md)
pages_to_fix = {
    'index.html': 'Boys Hostel & PG in Rau, Indore',
    'amenities.html': 'Premium Amenities | Boys Hostel',
    'rooms.html': 'Rooms & Pricing | Boys Hostel',
    'contact.html': 'Contact Us | Boys Hostel',
    'hostel-near-ips-academy.html': 'Boys Hostel Near IPS Academy',
    'hostel-near-medicaps-university.html': 'Hostel Near Medicaps University',
    'hostel-near-sd-bansal-college.html': 'Hostel Near SD Bansal College',
    'blog/benefits-of-living-in-hostel-vs-home.html': 'Benefits of Hostel vs Home',
    'blog/best-food-places-near-medicaps-university-rau.html': 'Best Food Places Near Medicaps',
    'blog/cost-of-living-in-rau-indore-for-students.html': 'Cost of Living in Rau for Students',
    'blog/hostel-vs-pg-vs-flat-for-students-indore.html': 'Hostel vs PG vs Flat Comparison',
    'blog/how-to-choose-best-hostel-in-indore.html': 'How to Choose Best Hostel',
    'blog/medicaps-university-review-admission-placement.html': 'Medicaps University Review',
    'blog/student-life-in-rau-indore-guide.html': 'Student Life in Rau Guide',
    'blog/top-colleges-in-rau-indore.html': 'Top Colleges in Rau, Indore',
    'blog/ips-academy-indore-review-guide.html': 'IPS Academy Indore Review',
}

def fix_title(filepath, new_title):
    """Fix title in HTML file"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Find and replace the title tag
        old_title_match = re.search(r'<title>.*?</title>', content, re.DOTALL)
        if old_title_match:
            old_title = old_title_match.group(0)
            
            # Add Radiance Residency suffix for most pages
            if 'Radiance Residency' not in new_title:
                new_title_tag = f'<title>{new_title} | Radiance Residency</title>'
            else:
                new_title_tag = f'<title>{new_title}</title>'
            
            new_content = content.replace(old_title, new_title_tag)
            
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            
            title_chars = len(new_title_tag) - 15  # Remove <title></title> length
            print("[OK] %s" % filepath)
            print("     Length: %d chars" % title_chars)
            return True
        else:
            print("[SKIP] %s - No title tag found" % filepath)
            return False
    except Exception as e:
        print("[ERROR] %s - %s" % (filepath, str(e)))
        return False

# Process all files
print("Starting title fixes...\n")
fixed = 0
for filepath, new_title in pages_to_fix.items():
    if os.path.exists(filepath):
        if fix_title(filepath, new_title):
            fixed += 1
    else:
        print("[NOTFOUND] %s" % filepath)

print("\nFixed %d/%d files" % (fixed, len(pages_to_fix)))
