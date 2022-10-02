import json
import wget
import requests
import csv
import pandas as pd
import calendar
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

# 获取指定用户关注列表
def GetUserFollowingList(User, DownloadAccountPicture=False):
    FollowingList = []
    requests.packages.urllib3.disable_warnings(InsecureRequestWarning) #禁用SSL证书验证警告
    ApiURL = "https://api.github.com/users/"+User+"/following"
    InitJson = requests.get(url=ApiURL, verify=False).text
    LoadJson = json.loads(InitJson, strict=False)
    try:
        if LoadJson["message"] == "Not Found":
            return(1)
    except:
        pass
    if bool(DownloadAccountPicture) == False:
        try:
            x = 0
            while True:
                FollowingList.append(LoadJson[x]["login"])
                x += 1
        except IndexError:
            return(FollowingList)
        except:
            return(1)
    else:
        try:
            x = 0
            while True:
                FollowingList.append(LoadJson[x]["login"])
                PictureURL = LoadJson[x]["avatar_url"]
                PictureName = LoadJson[x]["login"]+".jpg"
                wget.download(PictureURL, out=PictureName)
                x += 1
        except IndexError:
            return(FollowingList)
        except:
            return(1)

# 获取指定用户被关注列表
def GetUserFollowersList(User, DownloadAccountPicture=False):
    FollowersList = []
    requests.packages.urllib3.disable_warnings(InsecureRequestWarning) #禁用SSL证书验证警告
    ApiURL = "https://api.github.com/users/"+User+"/followers"
    InitJson = requests.get(url=ApiURL, verify=False).text
    LoadJson = json.loads(InitJson, strict=False)
    try:
        if LoadJson["message"] == "Not Found":
            return(1)
    except:
        pass
    if bool(DownloadAccountPicture) == False:
        try:
            x = 0
            while True:
                FollowersList.append(LoadJson[x]["login"])
                x += 1
        except IndexError:
            return(FollowersList)
        except:
            return(1)
    else:
        try:
            x = 0
            while True:
                FollowersList.append(LoadJson[x]["login"])
                PictureURL = LoadJson[x]["avatar_url"]
                PictureName = LoadJson[x]["login"]+".jpg"
                wget.download(PictureURL, out=PictureName)
                x += 1
        except IndexError:
            return(FollowersList)
        except:
            return(1)