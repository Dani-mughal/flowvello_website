import os
import glob
import re

SORA_LINK = '<link href="https://fonts.googleapis.com/css2?family=Sora:wght@100;200;300;400;500;600;700;800&display=swap" rel="stylesheet">'
PRECONNECT = '<link rel="preconnect" href="https://fonts.googleapis.com">\n    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'

BRAND_STYLE = """
<style>
/* --------------------------------------------------------------------------
   TECHTOX BRAND GUIDELINES TYPOGRAPHY — SORA ACROSS ALL WEIGHTS (100–800)
   Tracking: -10 (letter-spacing: -0.015em / -0.025em on display headings)
-------------------------------------------------------------------------- */
body, h1, h2, h3, h4, h5, h6, p, span, a, li, button, input, label, div, section {
   font-family: 'Sora', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif !important;
   letter-spacing: -0.015em;
}
h1, h2, h3, h4, h5, h6, .vibe-heading {
   font-family: 'Sora', sans-serif !important;
   letter-spacing: -0.025em !important;
   font-weight: 700;
}
.fv-page-hero h1 {
   font-family: 'Sora', sans-serif !important;
   letter-spacing: -1.5px !important;
   font-weight: 700 !important;
}
.fv-page-hero .fv-eyebrow, .vibe-eyebrow {
   font-family: 'Sora', sans-serif !important;
   letter-spacing: 2px !important;
   font-weight: 700 !important;
   text-transform: uppercase !important;
}
.fv-page-hero .fv-lead, .vibe-lead {
   font-family: 'Sora', sans-serif !important;
   letter-spacing: -0.01em !important;
   font-weight: 400 !important;
}
</style>
"""

def update_file(filepath):
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()

    original = content

    # 1. Strip out Rubik and Teko Google Fonts link
    content = re.sub(r'<link[^>]*fonts\.googleapis\.com[^>]*family=[^>]*Rubik[^>]*>', '', content, flags=re.IGNORECASE)
    content = re.sub(r'<link[^>]*fonts\.googleapis\.com[^>]*family=[^>]*Teko[^>]*>', '', content, flags=re.IGNORECASE)

    # 2. Ensure Sora Google Fonts link is present
    if 'fonts.googleapis.com/css2?family=Sora' not in content:
        # insert after <head> or <title>
        if '<head>' in content:
            content = content.replace('<head>', f'<head>\n    {PRECONNECT}\n    {SORA_LINK}', 1)
        elif '</title>' in content:
            content = content.replace('</title>', f'</title>\n    {SORA_LINK}', 1)

    # 3. Replace inline or in-tag font-families: Rubik, Teko, Inter, Poppins, Outfit
    content = re.sub(r"font-family:\s*['\"]?Rubik['\"]?(?:,\s*sans-serif)?(?: !important)?;", "font-family: 'Sora', sans-serif !important;", content, flags=re.IGNORECASE)
    content = re.sub(r"font-family:\s*['\"]?Teko['\"]?(?:,\s*sans-serif)?(?: !important)?;", "font-family: 'Sora', sans-serif !important;", content, flags=re.IGNORECASE)
    content = re.sub(r"font-family:\s*['\"]?Inter['\"]?(?:,\s*sans-serif)?(?: !important)?;", "font-family: 'Sora', sans-serif !important;", content, flags=re.IGNORECASE)
    content = re.sub(r"font-family:\s*['\"]?Poppins['\"]?(?:,\s*sans-serif)?(?: !important)?;", "font-family: 'Sora', sans-serif !important;", content, flags=re.IGNORECASE)
    content = re.sub(r"font-family:\s*['\"]?Outfit['\"]?(?:,\s*sans-serif)?(?: !important)?;", "font-family: 'Sora', sans-serif !important;", content, flags=re.IGNORECASE)

    # 4. Inject brand typography style if not already present
    if 'TECHTOX BRAND GUIDELINES TYPOGRAPHY' not in content:
        # inject right before </head>
        if '</head>' in content:
            content = content.replace('</head>', f'{BRAND_STYLE}\n</head>', 1)

    if content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    return False

# Target all service pages
service_pages = sorted(glob.glob('services/*.html'))
updated_services = 0
for sp in service_pages:
    # check if it's a redirect stub
    with open(sp, 'r', encoding='utf-8', errors='ignore') as f:
        c = f.read()
    if 'http-equiv="refresh"' in c:
        continue # skip redirect files
    
    if update_file(sp):
        updated_services += 1
        print(f"Updated brand typography: {sp}")
    else:
        print(f"Already brand-compliant: {sp}")

print(f"\nTotal service pages updated: {updated_services}")

# Also update services.html
if update_file('services.html'):
    print("Updated brand typography: services.html")
