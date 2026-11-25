with open("logo_b64.txt", "r", encoding="utf-8") as f:
    b64 = f.read().strip()

with open("logo_data.js", "w", encoding="utf-8") as f:
    f.write(f'const LOGO_BASE64 = "data:image/jpeg;base64,{b64}";\n')

print("Created logo_data.js successfully!")
