import glob
from html.parser import HTMLParser

class Validator(HTMLParser):
    def __init__(self):
        super().__init__()
        self.stack = []
        self.void_tags = {'area', 'base', 'br', 'col', 'embed', 'hr', 'img', 'input', 'link', 'meta', 'param', 'source', 'track', 'wbr'}
    def handle_starttag(self, tag, attrs):
        if tag not in self.void_tags:
            self.stack.append(tag)
    def handle_endtag(self, tag):
        if tag not in self.void_tags:
            if self.stack and self.stack[-1] == tag:
                self.stack.pop()

all_ok = True
for fpath in ['index.html', 'services.html'] + glob.glob('services/*.html'):
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()
    v = Validator()
    v.feed(content)
    if v.stack:
        print(f"FAILED: {fpath} unclosed tags: {v.stack}")
        all_ok = False

if all_ok:
    print("SUCCESS: All HTML files are structurally valid with 0 unclosed tags.")
