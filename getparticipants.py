import pyrebase
import csv

config = {
    'apiKey': "AIzaSyAZHCLuovX2oNhccuxjetkHNgAcrWcZLGo",
    'authDomain': "dhisna-ac7e0.firebaseapp.com",
    'databaseURL': "https://dhisna-ac7e0.firebaseio.com",
    'projectId': "dhisna-ac7e0",
    'storageBucket': "dhisna-ac7e0.appspot.com",
    'messagingSenderId': "1079389260336",
    "serviceAccount": "dhisna-ac7e0-firebase-adminsdk-4nede-35ccecd4ea.json"
}

firebase = pyrebase.initialize_app(config)

db = firebase.database()
event = "VLSI" #change the event here
results = db.child("registration/").child(event)


resu = results.get()
res = resu.val()
users = db.child("users/")
us = users.get()
user= us.val()
lines = [["name","email"]]
for i in res:
    if res[i]!="paid":
        print(user[i])
        lines.append([i,user[i]["email"]])

print(lines)

with open('people.csv', 'w',newline="") as writeFile:
    writer = csv.writer(writeFile)
    writer.writerows(lines)

writeFile.close()