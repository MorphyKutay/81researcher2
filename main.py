import os
import time
import requests

print("""

         ⠀⣰⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ ⠀⠀⠀⠀  ⠀⠐⣆⠀⠀
 ⣴⠁⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ ⠀⠀⠀⠀ ⠀ ⢀⠃⢣⠀
 ⢻⠀⠸⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ ⠀⠀⠀⠀  ⠀⡜⠀⢸⠇
 ⠘⡄⢆⠑⡄⠀⠀⠀⠀⠀⢀⣀⣀⣠⣄⣀⣀⡀⠀⠀ ⠀⠀ ⢀⠜⢠⢀⡆⠀
 ⠀⠘⣜⣦⠈⢢⡀⣀⣴⣾⣿⡛⠛⠛⠛⠛⠛⡿⣿⣦⣄⡠⠋⣰⢧⠎⠀⠀
⠀ ⠀⠘⣿⣧⢀⠉⢻⡟⠁⠙⠃⠀⠀⠀⠀⠈⠋⠀⠹⡟⠉⢠⢰⣿⠏⠀⠀⠀
⠀⠀ ⠀⠘⣿⡎⢆⣸⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⣿⣠⢣⣿⠏⠀⠀⠀⠀
⠀⠀ ⠀⡖⠻⣿⠼⢽⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⠹⣾⠟⢳⡄⠀⠀⠀
⠀⠀ ⠀⡟⡇⢨⠀⢸⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡎⠀⣇⢠⢿⠇⠀⠀⠀
⠀⠀ ⠀⢹⠃⢻⡤⠚⠀⠀⠀⠀⣀⠀⠀⢀⠀⠀⠀⠀⠙⠢⡼⠀⢻⠀⠀⠀⠀
⠀⠀ ⠀⠸⡓⡄⢹⠦⠤⠤⠤⢾⣇⠀⠀⢠⡷⠦⠤⠤⠴⢺⢁⠔⡟⠀⠀⠀⠀
⠀⠀ ⠀⢠⠁⣷⠈⠓⠤⠤⠤⣞⡻⠀⠀⢸⣱⣤⠤⠤⠔⠁⣸⡆⣇⠀⠀⠀⠀
⠀⠀ ⠀⠘⢲⠋⢦⣀⣠⢴⠶⠀⠁⠀⠀⠈⠁⠴⣶⣄⣀⡴⠋⣷⠋⠀⠀⠀⠀
⠀⠀ ⠀⠀⣿⡀⠀⠀⢀⡘⠶⣄⡀⠀⠀⠀⣠⡴⠞⣶⠀⢀⠀⣼⠀⠀⠀⠀⠀
⠀⠀ ⠀⠀⠈⠻⣌⢢⢸⣷⣸⡈⠳⠦⠤⠞⠁⣷⣼⡏⣰⢃⡾⠋⠀⠀⠀⠀⠀
⠀⠀ ⠀⠀⠀⠀⠙⢿⣿⣿⡇⢻⡶⣦⣤⡴⡾⢸⣿⣿⣷⠏⠀⠀⠀⠀⠀⠀⠀
⠀⠀ ⠀⠀⠀⠀⠀⠀⢿⡟⡿⡄⣳⣤⣤⣴⢁⣾⠏⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀ ⠀⠀⠀⠀⠀⠀⠈⣷⠘⠒⠚⠉⠉⠑⠒⠊⣸⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀ ⠀⠀⠀⠀⠀⠀⠀⠈⠳⠶⠔⠒⠒⠲⠴⠞⠋⠀⠀



81rsc2 By KutaySec
""")


#-------------
apk = input("apk ismini giriniz : ")

print("\napk decompile ediliyor...\n")
time.sleep(5)

os.system("apktool d "+apk)

path = apk.strip('.apk')

# api key scanner
value = path+"/res/values/strings.xml"
with open(value, "r") as file:
    content = file.read()
    if "google_api_key" in content:
        start_index = content.index("google_api_key") + len("google_api_key") + 1
        end_index = content.find("\n", start_index)
        api_key = content[start_index:end_index].strip()
        print("API anahtarı:", api_key)
        url = 'https://www.googleapis.com/identitytoolkit/v3/relyingparty/verifyPassword?key='+api_key
        headers = {'content-type': 'application/json', 'Accept-Charset': 'UTF-8'}
        r = requests.post(url, headers=headers)
        if r.status_code == 200:
            print("[+] It was possible to obtain an authentication token : "+api_key)
        else:
            print("[-] api key oturum hataya uğradı")
    else:
         print("\nAPI anahtarı bulunamadı!\n")
# ---------- firebase ---------
value2 = path+"/AndroidManifest.xml"
with open(value2, "r") as file:
    content = file.read()
    if "firebase" in content:
        start_index = content.index("firebase") + len("firebase") + 1
        end_index = content.find("\n", start_index)
        fire_base = content[start_index:end_index].strip()
        print("Firebase bulundu\n")
        value3 = path+"/res/values/strings.xml"
        with open(value3, 'r'):
            content = file.read()
            if "project_id" in content:
                start_index = content.index("project_id") + len("project_id") + 1
                end_index = content.find("\n", start_index)
                project_id = content[start_index:end_index].strip()
                print("project_id bulundu : ",project_id)
                url = 'https://firestore.googleapis.com/v1beta1/projects/'+project_id+'/databases/(default)/documents/"'
                headers = {'content-type': 'application/json', 'Accept-Charset': 'UTF-8'}
                r = requests.post(url,headers=headers)
                if r.status_code == 200:
                    print("koleksiyon okunabilir")
                else:
                    print("koleksiyon okunamaz")
            else:
                print("project_id bulunamadı\n")
    else:
         print("Firebase ve project_id bulunamadı\n")
#------------

