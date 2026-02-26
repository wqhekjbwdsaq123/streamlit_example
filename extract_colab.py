import urllib.request
import json
import sys

url = 'https://drive.google.com/uc?id=13sdsrsjFoc-_uHA5IaG_OTSPM7C9jhEc&export=download'

try:
    res = urllib.request.urlopen(url)
    data = json.loads(res.read().decode('utf-8'))
except Exception as e:
    print(f"Error downloading or parsing JSON: {e}")
    sys.exit(1)

with open('app.py', 'w', encoding='utf-8') as f:
    for cell in data.get('cells', []):
        if cell.get('cell_type') == 'code':
            source = cell.get('source', [])
            f.write(''.join(source) + '\n\n')

print("Extraction complete.")
