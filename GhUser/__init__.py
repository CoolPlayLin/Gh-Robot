import json
import wget
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning

# 获取指定用户头像
def GetUserAccountPicture(User, UseWgetDownload):
    if UseWgetDownload == True:
        pass
    elif UseWgetDownload == False:
        pass
    else:
        return("VE")
    requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
    ApiURL = "https://api.github.com/users/"+User
    InitJson = requests.get(url=ApiURL, verify=False).text
    LoadJson = json.loads(InitJson, strict=False)
    PictureURL = LoadJson["avatar_url"]
    if UseWgetDownload == False:
        try:
            return(PictureURL)
        except:
            return("FNT")
    else:
        wget.download(PictureURL, out="Account.jpg")

# 获取指定用户关注列表
def GetUserFollowingList(User, DownloadAccountPicture):
    FollowingList = []
    if DownloadAccountPicture == True:
        pass
    elif DownloadAccountPicture == False:
        pass
    else:
        return("VE")
    requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
    ApiURL = "https://api.github.com/users/"+User+"/following"
    InitJson = requests.get(url=ApiURL, verify=False).text
    LoadJson = json.loads(InitJson, strict=False)
    try:
        if LoadJson["message"] == "Not Found":
            return("FNT")
    except:
        pass
    if DownloadAccountPicture == False:
        try:
            x = 0
            while True:
                FollowingList.append(LoadJson[x]["login"])
                x += 1
        except:
            return(FollowingList)
    else:
        try:
            x = 0
            while True:
                FollowingList.append(LoadJson[x]["login"])
                PictureURL = LoadJson[x]["avatar_url"]
                PictureName = LoadJson[x]["login"]+".jpg"
                wget.download(PictureURL, out=PictureName)
                x += 1
        except:
            return(FollowingList)

# 获取指定用户被关注列表
def GetUserFollowersList(User, DownloadAccountPicture):
    FollowersList = []
    if DownloadAccountPicture == True:
        pass
    elif DownloadAccountPicture == False:
        pass
    else:
        return("VE")
    requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
    ApiURL = "https://api.github.com/users/"+User+"/followers"
    InitJson = requests.get(url=ApiURL, verify=False).text
    LoadJson = json.loads(InitJson, strict=False)
    try:
        if LoadJson["message"] == "Not Found":
            return("FNT")
    except:
        pass
    if DownloadAccountPicture == False:
        try:
            x = 0
            while True:
                FollowersList.append(LoadJson[x]["login"])
                x += 1
        except:
            return(FollowersList)
    else:
        try:
            x = 0
            while True:
                FollowersList.append(LoadJson[x]["login"])
                PictureURL = LoadJson[x]["avatar_url"]
                PictureName = LoadJson[x]["login"]+".jpg"
                wget.download(PictureURL, out=PictureName)
                x += 1
        except:
            return(FollowersList)


print(GetUserFollowersList("CoolPlayLin", DownloadAccountPicture=True))