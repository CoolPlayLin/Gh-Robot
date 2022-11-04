import setuptools

# 读取README文件
while True:
    try:
        with open("README.md", "r", encoding="utf-8") as fh:
            long_description = fh.read()
        break
    except:
        with open(r".\docs\README.md", "r", encoding="utf-8") as fh:
            with open("README.md", "w+", encoding="utf-8") as writer:
                writer.write(fh.read())

# 设置主体
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
