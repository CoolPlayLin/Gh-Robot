import requests
import json
from requests.packages.urllib3.exceptions import InsecureRequestWarning

# 获取所有Latest-Release链接
def GetAllLatestDownloadURL(User, Repo, Select=None, TXT=False):
  requests.packages.urllib3.disable_warnings(InsecureRequestWarning) #禁用SSL证书验证警告
  UrlList = []
  ApiURL="https://api.github.com/repos/{}/{}/releases/latest".format(User, Repo)
  IntJson = requests.get(url=ApiURL, verify=False).text
  LoadJson = json.loads(IntJson, strict=False)
  if bool(TXT) is False:
    if bool(Select) is False:
      try:
          x = 0
          while True:
              UrlList.append(LoadJson["assets"][x]["browser_download_url"])
              x += 1
      except (IndexError, KeyError):
        return(UrlList)
    else:
      try:
        x = 0
        while True:
          Cache = LoadJson["assets"][x]["browser_download_url"]
          if Select in Cache:
            UrlList.append(LoadJson["assets"][x]["browser_download_url"])
          x += 1
      except (IndexError, KeyError):
        return(UrlList)
  else:
    if type(TXT) == bool:
      TheFileNameWrittenToTXT = "Urls.txt"
    else:
      TheFileNameWrittenToTXT = str(TXT)
    if bool(Select) is False:
      with open(TheFileNameWrittenToTXT, "w+", newline="", encoding="utf-8") as file:
        try:
          x = 0
          while True:
            file.write(LoadJson["assets"][x]["browser_download_url"]+"\n")
            x += 1
        except (IndexError, KeyError):
          return(0)
    else:
      with open(TheFileNameWrittenToTXT, "w+", newline="", encoding="utf-8") as file:
        try:
          x = 0
          while True:
            if Select in LoadJson["assets"][x]["browser_download_url"]:
              file.write(LoadJson["assets"][x]["browser_download_url"]+"\n")
            x += 1
        except (IndexError, KeyError):
          return(0)

# 获取指定Latest-Release链接
def GetLatestDownloadURL(User, Repo, Order):
  requests.packages.urllib3.disable_warnings(InsecureRequestWarning) #禁用SSL证书验证警告
  ApiURL="https://api.github.com/repos/{}/{}/releases/latest".format(User, Repo)
  IntJson = requests.get(url=ApiURL, verify=False).text
  LoadJson = json.loads(IntJson, strict=False)
  try:
    return(LoadJson["assets"][Order]["browser_download_url"])
  except Exception as Error:
      print(Error)
      return(1)