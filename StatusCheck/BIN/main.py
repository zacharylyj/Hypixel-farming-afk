##################################
#                                #
#        Status Checker          #
#           zacweee              #
#                                #
##################################

from multiprocessing.connection import wait
import time
import requests
import json

DETAILS = open("DETAILS.json", "r").read()
API_KEY = json.loads(DETAILS)["API_KEY"]
zacweee = json.loads(DETAILS)["zacweee"]
duckzzq = json.loads(DETAILS)["duckzzq"]
uoshua = json.loads(DETAILS)["uoshua"]
kewnd = json.loads(DETAILS)["kewnd"]

def get_info(call):
    r = requests.get(call)
    return r.json()

def locationCheck(userid):
    if((get_info(f"https://api.hypixel.net/status?key={API_KEY}&uuid={userid}")["session"]["online"]) == False):
        return 1
    elif((get_info(f"https://api.hypixel.net/status?key={API_KEY}&uuid={userid}")["session"]["gameType"]) == "SKYBLOCK" and (get_info(f"https://api.hypixel.net/status?key={API_KEY}&uuid={userid}")["session"]["mode"]) == "dynamic"):
        return 2
    else:
        return 0
    
def get_status(username):
    userid = username
    temp = locationCheck(userid)
    if temp == 0:
        return "Online Limbo"
    elif temp == 1:
        return "Offline"
    elif temp == 2:
        return "Online AFKing"

def main():
    print(f"zacweee: {get_status(zacweee)}")
    print(f"duckzzq: {get_status(duckzzq)}")
    print(f"uoshua:  {get_status(uoshua)}")
    print(f"kewnd:   {get_status(kewnd)}")
    time.sleep(5)

if((get_info(f"https://api.hypixel.net/status?key={API_KEY}&uuid={zacweee}")["success"]) == False):
    API_KEY = input("API: ")
    updatejson = {
    "API_KEY": API_KEY,
    "zacweee": "a35b018c7eac4a90a6c7a6ba3d0026c8",
    "duckzzq": "467532119c4e42bc9cfb879324ea5bda",
    "uoshua": "0de03707bc584ca1899388a7c1cea215",
    "kewnd": "40f2878e755f4f52a9db1acb85bf2458"
}
    jsonString = json.dumps(updatejson)
    jsonFile = open("Details.json", "w")
    jsonFile.write(jsonString)
    jsonFile.close()

main()