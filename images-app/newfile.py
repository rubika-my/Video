import os
import urllib.parse
import re

folder_path = "."

def remove_invisible_chars(name):
    pattern = r'[\u200B-\u200F\u202A-\u202E]'
    return re.sub(pattern, '', name)

def clean_filename(name):
    name = urllib.parse.unquote(name)
    name = remove_invisible_chars(name)
    name = ''.join(c for c in name if c.isprintable())
    name = re.sub(r'[<>:"/\\|?*]', '_', name)
    name = name.strip()
    return name

print("شروع اصلاح نام فایل‌ها...\n")

for filename in os.listdir(folder_path):
    full_path = os.path.join(folder_path, filename)
    if os.path.isfile(full_path):
        new_name = clean_filename(filename)
        if new_name != filename:
            # ابتدا یک نام موقت می‌دهیم تا سیستم فایل تغییر را بپذیرد
            tmp_name = "tmp_rename_" + filename
            tmp_full_path = os.path.join(folder_path, tmp_name)
            try:
                os.rename(full_path, tmp_full_path)
                final_full_path = os.path.join(folder_path, new_name)
                os.rename(tmp_full_path, final_full_path)
                print(f"Renamed: '{filename}' -> '{new_name}'")
            except Exception as e:
                print(f"Failed to rename '{filename}': {e}")

print("\nتمام نام فایل‌ها اصلاح شد.")