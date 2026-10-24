with open('css/custom.css', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, l in enumerate(lines[:80]):
    print(l, end='')
