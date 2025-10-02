import os
import urllib.parse

# مسیر پوشه (در صورتی که عکس‌ها و کد در یک محل هستند، می‌توانید "." بگذارید)
folder_path = "."

# لیست تمام فایل‌ها در پوشه
for filename in os.listdir(folder_path):
    # مسیر کامل فایل
    full_path = os.path.join(folder_path, filename)
    
    # فقط فایل‌ها را پردازش می‌کنیم
    if os.path.isfile(full_path):
        # decode نام فایل
        decoded_name = urllib.parse.unquote(filename)
        
        # اگر نام decode شده متفاوت بود، تغییر بده
        if decoded_name != filename:
            new_full_path = os.path.join(folder_path, decoded_name)
            # تغییر نام فایل
            os.rename(full_path, new_full_path)
            print(f"Renamed: '{filename}' -> '{decoded_name}'")