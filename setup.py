import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Gh-Robots",
    version="V0.0.4.8",
    author="CoolPlayLin",
    author_email="help@api-coolplaylin.eu.org",
    description="A Github API-based Robot",
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=setuptools.find_packages(),
    license='GPL V3.0',
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
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)"
    ]
)