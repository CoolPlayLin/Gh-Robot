import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Gh-Robots",
    version="V0.0.2.2",
    author="CoolPlayLin",
    author_email="help@api-coolplaylin.eu.org",
    description="A Github API-based Robot",
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=setuptools.find_packages(),
    license='GPL V3.0',
    project_urls={
        "Bug Report": "https://github.com/CoolPlayLin/Gh-Robot/issues/new/choose"
    },
    url="https://github.com/CoolPlayLin/Gh-Robot",
    install_requires=[
        'requests==2.28.1'
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)"
    ]
)