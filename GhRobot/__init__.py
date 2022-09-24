import requests
import json
from requests.packages.urllib3.exceptions import InsecureRequestWarning


# 获取所有Release链接
def GetAllLatestDownloadURL(User, Repo):
    UrlList = []
    requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
    ApiURL="https://api.github.com/repos/"+User+"/"+Repo+"/releases/latest"
    IntJson = requests.get(url=ApiURL, verify=False).text
    LoadJson = json.loads(IntJson, strict=False)
    try:
      if LoadJson["message"] == "Not Found":
        print("Related files not found")
        exit(1)
    except:
      pass
    else:
        pass
    try:
        x = 0
        while True:
            UrlList.append(LoadJson["assets"][x]["browser_download_url"])
            x += 1
    except:
        pass
    return(UrlList)