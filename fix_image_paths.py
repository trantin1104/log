import os
import re

# Thư mục content của Hugo
CONTENT_DIR = "content"

# Regex để tìm <img src="/images/...">
pattern = re.compile(r'<img\s+[^>]*src="(/images/[^"]+)"([^>]*)>', re.IGNORECASE)

def fix_image_paths():
    for root, _, files in os.walk(CONTENT_DIR):
        for file in files:
            if file.endswith(".md") or file.endswith(".markdown"):
                path = os.path.join(root, file)
                
                with open(path, "r", encoding="utf-8") as f:
                    content = f.read()

                # Thay đường dẫn ảnh
                new_content = pattern.sub(
                    lambda m: f'<img src="{{{{ "{m.group(1)}" | relURL }}}}"{m.group(2)}>',
                    content
                )

                # Ghi lại nếu có thay đổi
                if new_content != content:
                    with open(path, "w", encoding="utf-8") as f:
                        f.write(new_content)
                    print(f"✔ Fixed: {path}")

if __name__ == "__main__":
    fix_image_paths()
    print("🎉 Done! All image paths have been fixed.")
