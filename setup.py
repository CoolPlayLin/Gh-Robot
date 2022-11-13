"""
This file is only for library packaging, if you are not a professional, please do not modify this file, because the modification may cause packaging failure or other problems.
"""
try:
    import setuptools
    import os
    import time
except Exception as Error:
    print("Program initialization error.")
    print(Error)
    exit(1)

# 运行必须变量
RUN = True
READMEFile = "README.md"
Any_Error = False
Debug = True
DocsPath = "./docs/"
long_description = None
TIMEFormat = "%Y-%m-%d %H:%M:%S"

def DebugLogger(Error=None, Event=None, Warning=None, Template=None):
    global Debug
    global TIMEFormat

    if Debug:
        with open("Build.log", "a", encoding="utf-8") as Pen: 
            try:
                if Event is not None:
                    Pen.writelines("{} Event: {}".format(time.strftime(TIMEFormat), Event))
                if Warning is not None:
                    Pen.writelines("{} Warning: {}".format(time.strftime(TIMEFormat), Warning))
                if Error is not None:
                    Pen.writelines("{} Error: {}".format(time.strftime(TIMEFormat), Error))
                if Template is not None and type(Template) == int:
                    if Template == 0:
                        Pen.writelines("All Done")
                    elif Template == 1:
                        Pen.writelines("The program exits abnormally.")
                    Pen.writelines("\n")
            except Exception as Error:
                Pen.writelines("{} An error occurred with the logger: {}\n".format(time.strftime(TIMEFormat) ,Error))
            Pen.writelines("\n")

def RUNStatus():
    global Any_Error

    if Any_Error:
        DebugLogger(Template=1)
        exit(1)
    else:
        DebugLogger(Template=0)
        return 0

# 运行清理
def Clean():
    global READMEFile

    DebugLogger(Event="Cleanup is running")
    try:
        os.remove(READMEFile)
        DebugLogger(Event="Cleanup completed successfully")
    except:
        DebugLogger(Warning="An error occurred while cleaning the file")
    return 0

def SetupDate():
    global long_description
    DebugLogger(Event="The SetupDate function is successfully called")
    setuptools.setup(
            name="Gh-Robots",
            version="0.0.5",
            author="CoolPlayLin",
            author_email="help@api-coolplaylin.eu.org",
            description="A Github API-based Robot",
            long_description=long_description,
            long_description_content_type='text/markdown',
            packages=setuptools.find_packages(),
            license='GPL',
            project_urls={
                "Bug Report": "https://github.com/CoolPlayLin/Gh-Robot/issues/new?assignees=&labels=bug&template=bug_report.md&title=%5BBug%5D%3A",
                "Feature Request": "https://github.com/CoolPlayLin/Gh-Robot/issues/new?assignees=&labels=enhancement&template=feature-request.md&title=%5BFeature+Request%5D"
            },
            download_url="https://github.com/CoolPlayLin/Gh-Robot/releases",
            url="https://github.com/CoolPlayLin/Gh-Robot",
            install_requires=[
                'requests>=2.28.1',
                'wget>=3.2',
                'pandas>=1.5.0'
            ],
            classifiers=[
                "Development Status :: 2 - Pre-Alpha",
                "Natural Language :: English",
                "Programming Language :: Python :: 3",
                "Topic :: Software Development :: Libraries :: Python Modules",
                "License :: OSI Approved :: GNU General Public License v3 (GPLv3)"
            ]
        )
    DebugLogger(Event="The call to the SetupDate function completed successfully")
    return 0

def main():
    EndTimes = 0
    global RUN
    global READMEFile
    global DocsPath
    global Any_Error
    global Debug
    global long_description

    while RUN:
        if Any_Error or EndTimes >= 10:
            if EndTimes >= 10:
                DebugLogger(Error="The number of attempts to read/rebuild the README file has exceeded the limit")
            break

        try:
            with open(READMEFile, "r", encoding="utf-8") as fh:
                long_description = fh.read()
            RUN = False
            DebugLogger(Event="The README file read completed successfully")
        except FileNotFoundError as Error:
            DebugLogger(Warning=Error)
            try:
                DebugLogger(Warning="The README file failed to read, an attempt is being made to rebuild this file")
                with open(DocsPath+READMEFile, "r", encoding="utf-8") as fh:
                    with open(READMEFile, "w+", encoding="utf-8") as writer:
                        writer.write(fh.read())
                        DebugLogger(Event="The README file reconstruction completed successfully")
            except Exception as Error:
                DebugLogger(Error=Error)
                break
        except Exception as Error:
                DebugLogger(Error=Error)
                break
        EndTimes += 1
    else:
        if long_description is None:
            DebugLogger(Error="long_description value does not exist")
            Any_Error = True
            Clean()
            return 1
        else:
            SetupDate()
        return 0

    Clean()
    Any_Error = True
    return 1

if __name__ == "__main__":
    main()
    RUNStatus()