import os
import re

CONTENT_DIR = "content"

# Regex bắt tất cả các img có absURL
pattern = re.compile(r'(<img\s+[^>]*src="\{\{\s*"[^"]+"\s*\|\s*)absURL(\s*\}\}"[^>]*>)', re.IGNORECASE)

def fix_abs_to_rel():
    for root, _, files in os.walk(CONTENT_DIR):
        for file in files:
            if file.endswith(".md") or file.endswith(".markdown"):
                path = os.path.join(root, file)

                with open(path, "r", encoding="utf-8") as f:
                    content = f.read()

                # Thay absURL → relURL
                new_content = pattern.sub(lambda m: m.group(1) + "relURL" + m.group(2), content)

                if new_content != content:
                    with open(path, "w", encoding="utf-8") as f:
                        f.write(new_content)
                    print(f"✔ Fixed: {path}")

if __name__ == "__main__":
    fix_abs_to_rel()
    print("🎉 Done! All absURL have been replaced with relURL.")
