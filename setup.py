import setuptools
import os

# 运行必须变量
RUN = True
EndTimes = 0
READMEFile = "README.md"
Any_Error = False
Debug = False

def main():
    global EndTimes
    global RUN
    global READMEFile
    global Any_Error
    global Debug

    while RUN:
        if EndTimes > 5 or Any_Error:
            try:
                os.remove(READMEFile)
            except:
                pass
            return 1
        try:
            with open(READMEFile, "r", encoding="utf-8") as fh:
                long_description = fh.read()
            RUN = False
        except:
            try:
                with open(r"./docs/"+READMEFile, "r", encoding="utf-8") as fh:
                    with open(READMEFile, "w+", encoding="utf-8") as writer:
                        writer.write(fh.read())
            except Exception as Error:
                if Debug:
                    print(Error)
                Any_Error = True
        EndTimes += 1
    else:
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
        return 0

def RUNStatus():
    global EndTimes
    global Any_Error

    if EndTimes > 5 or Any_Error:
        exit(1)
    else:
        return 0

if __name__ == "__main__":
    main()
    RUNStatus()