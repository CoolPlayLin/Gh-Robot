@echo off
%1 mshta vbscript:CreateObject("Shell.Application").ShellExecute("cmd.exe","/c %~s0 ::","","runas",1)(window.close)&&exit
@echo off
cd /d %~dp0
pip install build
git clone https://github.com/CoolPlayLin/Gh-Robot
cd Gh-Robot
python -m build
pause