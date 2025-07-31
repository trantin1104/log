import os
import re

CONTENT_DIR = "content"
GITHUB_PREFIX = "/log"

# Hỗ trợ cả dạng có hoặc không dấu ngoặc kép ngoài
pattern = re.compile(
    r'<img\s+[^>]*src=["\']\{\{\s*"(/images/[^"]+)"\s*\|\s*relURL\s*\}\}["\'][^>]*>',
    re.IGNORECASE
)

for root, dirs, files in os.walk(CONTENT_DIR):
    for file in files:
        if file.endswith(".md"):
            filepath = os.path.join(root, file)
            with open(filepath, "r", encoding="utf-8") as f:
                content = f.read()

            # Thay thế <img ...> giữ nguyên width/align
            new_content = pattern.sub(
                lambda m: m.group(0)
                          .replace(m.group(0), f'<img src="{GITHUB_PREFIX}{m.group(1)}" width="70%">'),
                content
            )

            if new_content != content:
                with open(filepath, "w", encoding="utf-8") as f:
                    f.write(new_content)
                print(f"✅ Fixed: {filepath}")

print("Hoàn tất sửa tất cả ảnh!")
