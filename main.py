import os
import time

# degiskenler
apikey = "grep -i 'google_api_key' "

#-------------
apk = input("apk ismini giriniz : ")

print("apk decompile ediliyor...")
time.sleep(5)

os.system("apktool d "+apk)

path = apk.strip('.apk')

value = path+"/res/values/strings.xml"

with open(value, "r") as file:
    content = file.read()
    if "google_api_key" in content:
        start_index = content.index("google_api_key") + len("google_api_key") + 1
        end_index = content.find("\n", start_index)
        api_key = content[start_index:end_index].strip()
        print("API anahtarı:", api_key)
    else:
         print("HATA: API anahtarı bulunamadı!")
