import os
import re

# Thư mục content của Hugo
CONTENT_DIR = "content"

# Regex tìm relURL trong cú pháp Hugo
pattern = re.compile(r'\| *relURL *}}', re.IGNORECASE)

def fix_rel_to_abs():
    for root, _, files in os.walk(CONTENT_DIR):
        for file in files:
            if file.endswith(".md") or file.endswith(".markdown"):
                path = os.path.join(root, file)
                
                with open(path, "r", encoding="utf-8") as f:
                    content = f.read()

                # Đổi relURL -> absURL
                new_content = pattern.sub('| absURL }}', content)

                if new_content != content:
                    with open(path, "w", encoding="utf-8") as f:
                        f.write(new_content)
                    print(f"✔ Converted: {path}")

if __name__ == "__main__":
    fix_rel_to_abs()
    print("🎉 Done! All relURL have been converted to absURL.")
