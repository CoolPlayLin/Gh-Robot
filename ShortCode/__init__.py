import requests
import json

# 从URL获取JSON加载后输出
def GetAndLoadJsonFromURL(URL, UseLoadJSON, SSL):
    try:
        InitJSON = requests.get(url=URL, verify=bool(SSL))
    except:
        return(1)
    try:
        if bool(UseLoadJSON) == False:
            LoadedJSON = json.loads(InitJSON)
        elif bool(UseLoadJSON) == True:
            LoadedJSON = json.load(InitJSON)
    except:
        return(1)
    return(LoadedJSON)