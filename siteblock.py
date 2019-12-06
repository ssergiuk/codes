import time
from datetime import datetime as dm
hosts_temp = r"C:\Users\sserg\Desktop\APPS\site blocker\hosts"
hosts_path = r"C:\Windows\System32\drivers\etc\hosts"
redirect = "127.0.0.1"
website_list = ["www.facebook.com" , "facebook.com" , "instagram.com" , "www.instagram.com"]

while True:
    if  dm(dm.now().year, dm.now().month, dm.now().day, 8) < dm.now() < dm(dm.now().year, dm.now().month, dm.now().day, 18):
        with open(hosts_temp, "r+") as file:
            content = file.read()
            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write(redirect + "  " + website + "\n")

    else:
        with open(hosts_temp, "r+") as file:
            content = file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in website_list):
                    file.write(line)
            file.truncate()
    time.sleep(500)
