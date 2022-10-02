import requests
import json
from requests.packages.urllib3.exceptions import InsecureRequestWarning

# 从URL获取JSON加载后输出
def GetAndLoadJsonFromURL(URL, UseLoadJSON=False, SSL=True):
    if bool(SSL) == False:
        requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
    try:
        InitJSON = requests.get(url=URL, verify=bool(SSL)).text
    except requests.exceptions.SSLError as WhyError:
        print('\033[4;31m'+str(WhyError)+'\033[0m')
        return(1)
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