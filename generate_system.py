import os
import json

with open('logo_b64.txt', 'r', encoding='utf-8') as f:
    b64_logo = f.read().strip()

print("Loaded logo length:", len(b64_logo))
