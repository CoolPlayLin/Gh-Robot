import requests
import json
import csv
from requests.packages.urllib3.exceptions import InsecureRequestWarning

# 将用户全部的Repo数据导入到Repo.csv文件中
def GetAllRepoInformationToCSV(User):
    requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
    ApiURL = "https://api.github.com/users/" + User + "/repos"
    IntJson = requests.get(url=ApiURL, verify=False).text
    LoadJson = json.loads(IntJson, strict=False)
    try:
        if LoadJson["message"] == "Not Found":
            return("FNT")
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
    except:
        return(0)