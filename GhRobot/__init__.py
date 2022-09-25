import requests
import json
from requests.packages.urllib3.exceptions import InsecureRequestWarning


# 获取所有Latest-Release链接
def GetAllLatestDownloadURL(User, Repo):
  UrlList = []
  requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
  ApiURL="https://api.github.com/repos/"+User+"/"+Repo+"/releases/latest"
  IntJson = requests.get(url=ApiURL, verify=False).text
  LoadJson = json.loads(IntJson, strict=False)
  try:
    if LoadJson["message"] == "Not Found":
      return("FNT")
  except:
    pass
  try:
      x = 0
      while True:
          UrlList.append(LoadJson["assets"][x]["browser_download_url"])
          x += 1
  except:
      pass
  return(UrlList)

# 获取指定Latest-Release链接
def GetLatestDownloadURL(User, Repo, Order):
  requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
  ApiURL="https://api.github.com/repos/"+User+"/"+Repo+"/releases/latest"
  IntJson = requests.get(url=ApiURL, verify=False).text
  LoadJson = json.loads(IntJson, strict=False)
  try:
    if LoadJson["message"] == "Not Found":
      return("FNT")
  except:
    pass
  try:
    return(LoadJson["assets"][Order]["browser_download_url"])
  except:
    return("FNT")

# 获取指定格式Latest-Release链接
def GetFormatLatestDownloadURL(User, Repo, Format):
  UrlList = []
  requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
  ApiURL="https://api.github.com/repos/"+User+"/"+Repo+"/releases/latest"
  IntJson = requests.get(url=ApiURL, verify=False).text
  LoadJson = json.loads(IntJson, strict=False)
  try:
    if LoadJson["message"] == "Not Found":
      return("FNT")
  except:
    pass
  else:
      pass
  try:
    x = 0
    while True:
      Cache = LoadJson["assets"][x]["browser_download_url"]
      if Format in Cache:
        UrlList.append(LoadJson["assets"][x]["browser_download_url"])
      else:
        pass
      x += 1
  except:
      pass
  return(UrlList)