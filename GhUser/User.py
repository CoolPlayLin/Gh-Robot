import json
import wget
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning

# 获取指定用户头像
def GetUserAccountPicture(User, UseWgetDownload=False):
    requests.packages.urllib3.disable_warnings(InsecureRequestWarning) #禁用SSL证书验证警告
    ApiURL = "https://api.github.com/users/"+User
    InitJson = requests.get(url=ApiURL, verify=False).text
    LoadJson = json.loads(InitJson, strict=False)
    try:
        if LoadJson["message"] == "Not Found":
            return(1)
    except:
        pass
    PictureURL = LoadJson["avatar_url"]
    if bool(UseWgetDownload) == False:
        try:
            return(PictureURL)
        except:
            return(1)
    else:
        wget.download(PictureURL, out="Account.jpg")
        return(0)