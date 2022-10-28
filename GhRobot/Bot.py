import requests
import json
from requests.packages.urllib3.exceptions import InsecureRequestWarning

# 获取所有Latest-Release链接
def GetAllLatestDownloadURL(User, Repo, Format=None):
  requests.packages.urllib3.disable_warnings(InsecureRequestWarning) #禁用SSL证书验证警告
  UrlList = []
  if bool(Format) is False:
    ApiURL="https://api.github.com/repos/{}/{}/releases/latest".format(User, Repo)
    IntJson = requests.get(url=ApiURL, verify=False).text
    LoadJson = json.loads(IntJson, strict=False)
    try:
      if LoadJson["message"] == "Not Found":
        return(1)
    except:
      pass
    try:
        x = 0
        while True:
            UrlList.append(LoadJson["assets"][x]["browser_download_url"])
            x += 1
    except IndexError:
      return(UrlList)
    except Exception as WhyError:
      print(WhyError)
      return(1)
  else:
    ApiURL="https://api.github.com/repos/{}/{}/releases/latest".format(User, Repo)
    IntJson = requests.get(url=ApiURL, verify=False).text
    LoadJson = json.loads(IntJson, strict=False)
    try:
      if LoadJson["message"] == "Not Found":
        return(1)
    except:
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
    except IndexError:
      return(UrlList)
    except Exception as WhyError:
      print(WhyError)
      return(1)

# 获取指定Latest-Release链接
def GetLatestDownloadURL(User, Repo, Order):
  requests.packages.urllib3.disable_warnings(InsecureRequestWarning) #禁用SSL证书验证警告
  ApiURL="https://api.github.com/repos/"+User+"/"+Repo+"/releases/latest"
  IntJson = requests.get(url=ApiURL, verify=False).text
  LoadJson = json.loads(IntJson, strict=False)
  try:
    if LoadJson["message"] == "Not Found":
      return(1)
  except:
    pass
  try:
    return(LoadJson["assets"][Order]["browser_download_url"])
  except Exception as WhyError:
      print(WhyError)
      return(1)