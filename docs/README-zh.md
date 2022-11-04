# Gh-Robot

<p align="center">
<img src="https://cdn.api-go.asia/assets/img/Robot.png" width="50" height="50">
</p>

<p align="center">一个基于Github API的爬虫</p>


<p align="center">
<a href="https://github.com/CoolPlayLin/Gh-Robot/blob/main/LICENSE"><img src="https://img.shields.io/github/license/CoolPlayLin/Gh-Robot?style=flat-square"></a>
<a><img src="https://img.shields.io/pypi/dm/Gh-Robots?style=flat-square"></a>
<a href="https://pypi.org/project/Gh-Robots/"><img src="https://img.shields.io/pypi/v/Gh-Robots?style=flat-square"></a>
<a href="https://github.com/CoolPlayLin/Gh-Robot/pulls"><img src="https://img.shields.io/github/issues-pr/CoolPlayLin/Gh-Robot?style=flat-square"></a>
</p>

<p align="center">
<a>简体中文 </a>
·
<a href="./README.md">English</a>
</p>

##  **安装**

```
pip install Gh-Robots
```

[使用镜像站点](./Mirror.md)

# 🥰 本地构建

*你可以使用自动脚本或手动来进行本地构建*

## 手动构建

**克隆仓库**

```
git clone https://github.com/CoolPlayLin/Gh-Robot

cd Gh-Robot
```

**安装`Build`工具**
```
pip install build
```

**构建**
```
python -m build
```

切换版本
>*你可以通过这些命令来切换要构建的版本*

>**稳定版**
>```
>git checkout main
>```
>**开发版**
>```
>git checkout Dev
>```

## 自动脚本

**Linux**

[Main](https://cdn.api-go.asia/Auto/build-linux.sh)
[Dev](https://cdn.api-go.asia/Auto/build-Dev-linux.sh)

**Windows**

[Main](https://cdn.api-go.asia/Auto/build-win.bat)
[Dev](https://cdn.api-go.asia/Auto/build-Dev-win.bat)

**注意**

你的计算机必须安装有`Git`和带有`pip`的`Python`才能使用本脚本自动构建和手动构建