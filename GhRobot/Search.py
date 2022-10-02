import requests
import json
from requests.packages.urllib3.exceptions import InsecureRequestWarning

# 提取Repo搜索结果到JSON
def SearchRepo(Repo, Amount):
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
        x = 0
        while True:
            Project = {}
            Project["Name"] = LoadJSON["items"][x]["name"]
            Project["Author"] = LoadJSON["items"][x]["owner"]["login"]
            Project["URL"] = LoadJSON["items"][x]["html_url"]
            Date.append(Project)
            x += 1
    except IndexError:
        return(json.dumps(Date, ensure_ascii=False))
    except Exception as WhyError:
        print(WhyError)
        return(1)

# 提取User搜索结果到JSON
def SearchUser(User, Amount):
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
        x = 0
        while True:
            Project = {}
            Project["UserName"] = LoadJSON["items"][x]["login"]
            Project["Avatar"] = LoadJSON["items"][x]["avatar_url"]
            Project["HomePage"] = LoadJSON["items"][x]["html_url"]
            Date.append(Project)
            x += 1
    except IndexError:
        return(json.dumps(Date, ensure_ascii=False))
    except Exception as WhyError:
        print(WhyError)
        return(1)

# 生成指定数量的Repo搜索结果到JSON
def SearchManyRepo(Repo, Amount, Page):
    Date = []
    requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
    try:
        int(Page)
        int(Amount)
    except:
        pass
    if Amount * Page > 1000:
        return(1)
    i = 0
    while i <= Page:
        i += 1
        ApiURL = "https://api.github.com/search/repositories?q=" + Repo +"&per_page=" + str(int(Amount)) + "&page=" + str(i)
        InitJSON = requests.get(url=ApiURL, verify=False).text
        LoadJSON = json.loads(InitJSON)
        try:
            if bool(LoadJSON["message"]) == True:
                break
        except:
            pass
        try:
            x = 0
            while True:
                Project = {}
                Project["Name"] = LoadJSON["items"][x]["name"]
                Project["Author"] = LoadJSON["items"][x]["owner"]["login"]
                Project["URL"] = LoadJSON["items"][x]["html_url"]
                Date.append(Project)
                x += 1
        except IndexError:
            pass
        except KeyError:
            pass
    return(json.dumps(Date, ensure_ascii=False))

# 生成指定数量的User索结果到JSON
def SearchManyUser(User, Amount, Page):
    Date = []
    requests.packages.urllib3.disable_warnings(InsecureRequestWarning) #禁用SSL证书验证警告
    try:
        int(Page)
        int(Amount)
    except:
        pass
    if Amount * Page > 1000:
        return(1)
    i = 0
    while i <= Page:
        i += 1
        ApiURL = "https://api.github.com/search/users?q=" + User +"&per_page=" + str(int(Amount)) + "&page=" + str(i)
        InitJSON = requests.get(url=ApiURL, verify=False).text
        LoadJSON = json.loads(InitJSON)
        try:
            if bool(LoadJSON["message"]) == True:
                break
        except:
            pass
        try:
            x = 0
            while True:
                Project = {}
                Project["UserName"] = LoadJSON["items"][x]["login"]
                Project["Avatar"] = LoadJSON["items"][x]["avatar_url"]
                Project["HomePage"] = LoadJSON["items"][x]["html_url"]
                Date.append(Project)
                x += 1
        except IndexError:
            pass
        except KeyError:
            pass
    return(json.dumps(Date, ensure_ascii=False))
