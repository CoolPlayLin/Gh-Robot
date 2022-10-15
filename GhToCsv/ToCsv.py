import json
import requests
import csv
import calendar
from requests.packages.urllib3.exceptions import InsecureRequestWarning

# 将用户数据导入到CSV中
def GetUserDateToCSV(User):
    requests.packages.urllib3.disable_warnings(InsecureRequestWarning) #禁用SSL证书验证警告
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

# 将用户全部的Repo数据导入到Repo.csv文件中
def GetAllRepoInformationToCSV(User):
    requests.packages.urllib3.disable_warnings(InsecureRequestWarning) #禁用SSL证书验证警告
    ApiURL = "https://api.github.com/users/" + User + "/repos"
    IntJson = requests.get(url=ApiURL, verify=False).text
    LoadJson = json.loads(IntJson, strict=False)
    try:
        if LoadJson["message"] == "Not Found":
            return(1)
    except:
        pass
    try:
        with open("Repo.csv", "w", newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow([User+r"'s Repo"])
            writer.writerow(["Repo", "Description", "LICENSE", "FullName", "RepoURL", "GitUrl", "SshURL", "CloneURL"])
            x = 0
            while True:
                if bool(LoadJson[x]["license"]) == False:
                    LICENSES = "No LICENSE"
                else:
                    LICENSES = LoadJson[x]["license"]["name"]
                if bool(LoadJson[x]["description"]) == False:
                    DESCRIPTION = "No Description"
                else:
                    DESCRIPTION = LoadJson[x]["description"]
                writer.writerow([LoadJson[x]["name"], DESCRIPTION, LICENSES, LoadJson[x]["full_name"], LoadJson[x]["html_url"], LoadJson[x]["git_url"], LoadJson[x]["ssh_url"], LoadJson[x]["clone_url"]])
                x += 1
    except IndexError:
        return(0)
    except Exception as WhyError:
        print(WhyError)
        return(1)

# 提取Repo搜索结果到CSV
def SearchRepoToCSV(Repo, Amount):
    if bool(Amount) == False:
        ApiURL = "https://api.github.com/search/repositories?q=" + Repo
    elif bool(Amount) == True:
        try:
            if int(Amount) > 100:
                print("Github API supports a maximum of 100 pages, and the number you currently enter will not work")
            ApiURL = "https://api.github.com/search/repositories?q=" + str(Repo) + "&per_page=" + str(int(Amount))
        except:
            return(1)
    Date = []
    requests.packages.urllib3.disable_warnings(InsecureRequestWarning) #禁用SSL证书验证警告
    InitJSON = requests.get(url=ApiURL, verify=False).text
    LoadJSON = json.loads(InitJSON)
    if LoadJSON["total_count"] == 0:
        return(1)
    else:
        pass
    try:
        with open("RepoSearchResults.csv", "w", newline="", encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(["Name", "Author", "URL"])
            x = 0
            while True:
                writer.writerow([LoadJSON["items"][x]["name"], LoadJSON["items"][x]["owner"]["login"], LoadJSON["items"][x]["html_url"]])
                x += 1
    except IndexError:
        return(0)
    except Exception as WhyError:
        print(WhyError)
        return(1)

# 提取User搜索结果到CSV
def SearchUserToCSV(User, Amount):
    if bool(Amount) == False:
        ApiURL = "https://api.github.com/search/users?q=" + User
    elif bool(Amount) == True:
        try:
            if int(Amount) > 100:
                print("Github API supports a maximum of 100 pages, and the number you currently enter will not work")
            ApiURL = "https://api.github.com/search/users?q=" + str(User) + "&per_page=" + str(int(Amount))
        except:
            return(1)
    Date = []
    requests.packages.urllib3.disable_warnings(InsecureRequestWarning) #禁用SSL证书验证警告
    InitJSON = requests.get(url=ApiURL, verify=False).text
    LoadJSON = json.loads(InitJSON)
    if LoadJSON["total_count"] == 0:
        return(1)
    else:
        pass
    try:
        with open("UserSearchResults.csv", "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["UserName", "Avatar", "HomePage"])
            x = 0
            while True:
                writer.writerow([LoadJSON["items"][x]["login"], LoadJSON["items"][x]["avatar_url"], LoadJSON["items"][x]["html_url"]])
                x += 1
    except IndexError:
        return(0)
    except Exception as WhyError:
        print(WhyError)
        return(1)