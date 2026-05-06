import os
import re

files = [
    "anti-ragging.html", "bca-program.html", "clubs-activities.html",
    "infrastructure.html", "iqac.html", "rti.html",
    "sc-st-committee.html", "student-support.html"
]

pdf_link = """
                    <a href="downloads/AICTE-Mandatory-Disclosure.pdf" class="link-button" target="_blank">
                        View Official Publication (PDF)
                        <span class="material-symbols-outlined">picture_as_pdf</span>
                    </a>
"""

for f in files:
    with open(f, "r") as file:
        content = file.read()
    
    # If the file already has a link-button with smcp.ac.in, replace it
    if re.search(r'<a href="https://smcp\.ac\.in/page/.*?".*?</a>', content, re.DOTALL):
        content = re.sub(r'<a href="https://smcp\.ac\.in/page/.*?".*?</a>', pdf_link.strip(), content, flags=re.DOTALL)
    # If it doesn't have a link button but has <div class="content-box">
    elif 'class="content-box"' in content and "View Official Publication" not in content:
        # insert before the closing div of content-box
        content = re.sub(r'(</div>\s*</div>\s*</section>)', r'\n' + pdf_link + r'\n                \1', content)
    
    with open(f, "w") as file:
        file.write(content)

print("Done processing files.")
