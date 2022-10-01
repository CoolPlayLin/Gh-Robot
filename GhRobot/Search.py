import requests
import json
from requests.packages.urllib3.exceptions import InsecureRequestWarning

# 提取Repo搜索结果到JSON
def SearchRepo(Repo):
    Date = []
    requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
    ApiURL = "https://api.github.com/search/repositories?q=" + Repo
    InitJSON = requests.get(url=ApiURL, verify=False).text
    LoadJSON = json.loads(InitJSON, strict=False)
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

# 提取Repo搜索结果到JSON
def SearchUser(User):
    Date = []
    requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
    ApiURL = "https://api.github.com/search/users?q=" + User
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
