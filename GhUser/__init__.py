import json
import wget
import requests
import csv
import pandas as pd
import calendar
from requests.packages.urllib3.exceptions import InsecureRequestWarning

# 获取指定用户头像
def GetUserAccountPicture(User, UseWgetDownload):
    if bool(UseWgetDownload) == True:
        pass
    elif bool(UseWgetDownload) == False:
        pass
    requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
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
def GetUserFollowingList(User, DownloadAccountPicture):
    FollowingList = []
    if bool(DownloadAccountPicture) == True:
        pass
    elif bool(DownloadAccountPicture) == False:
        pass
    requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
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
def GetUserFollowersList(User, DownloadAccountPicture):
    FollowersList = []
    if bool(DownloadAccountPicture) == True:
        pass
    elif bool(DownloadAccountPicture) == False:
        pass
    requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
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

# 将用户数据导入到CSV中
def GetUserDateToCSV(User):
    requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
    ApiURL = "https://api.github.com/users/"+User
    InitJSON = requests.get(url=ApiURL, verify=False).text
    LoadJSON = json.loads(InitJSON, strict=False)
    try:
        if LoadJSON["message"] == "Not Found":
            return(1)
    except:
        pass
    try:
        with open("User.csv", "w", newline='', encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["UserName", "User", "Avatar","HomePage", "Company", "Blog", "Location", "Email", "Bio", "TwitterUsername", "Public Repos", "Public Gists", "Follower(s)", "Following", "Registration"])
            if bool(LoadJSON["company"]) == False:
                Company = "NO DATE"
            else:
                Company = LoadJSON["company"]
            if bool(LoadJSON["blog"]) == False:
                Blog = "NO DATE"
            else:
                Blog = LoadJSON["blog"]
            if bool(LoadJSON["location"]) == False:
                Location = "NO DATE"
            else:
                Location = LoadJSON["location"]
            if bool(LoadJSON["email"]) == False:
                Email = "NO DATE"
            else:
                Email = bool(LoadJSON["email"])
            if bool(LoadJSON["bio"]) == False:
                BIO = "NO DATE"
            else:
                BIO = LoadJSON["bio"]
            if bool(LoadJSON["twitter_username"]) == False:
                TwitterUsername = "NO DATE"
            else:
                TwitterUsername = LoadJSON["twitter_username"]
            RegistrationTime = calendar.month_name[pd.to_datetime(LoadJSON["created_at"]).month]+" "+str(pd.to_datetime(LoadJSON["created_at"]).day)+", "+str(pd.to_datetime(LoadJSON["created_at"]).year)
            writer.writerow([LoadJSON["name"], LoadJSON["login"], LoadJSON["avatar_url"], LoadJSON["html_url"], Company, Blog, Location, Email, BIO, TwitterUsername, str(LoadJSON["public_repos"]), str(LoadJSON["public_gists"]), str(LoadJSON["followers"]), str(LoadJSON["following"]), RegistrationTime])
            return(0)
    except:
        return(1)