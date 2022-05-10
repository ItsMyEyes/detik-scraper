from setuptools import setup, find_packages

classifiers = [
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3.9',
    'Programming Language :: Python :: 3 :: Only',
    'Topic :: Software Development :: Libraries :: Python Modules',
]

markdownData = """
# Detik Scrapper

## Installation
- Install package
After cloning, go to directory and run this command for installation package
```
$ pip install detik-scrapper
```
- Then you test it with new file like main.py / Example Code
```
import detik
import json

print(json.dumps(detik.getListHotNews(), indent=4))
```

## Available Function
* List Category
```
getListCategory() -> dict
```

* List New By Category Name
```
getListNews(category: str) -> dict:
```

* List Hot News
```
getListHotNews() -> dict:
```

* Detail News
```
getDetailNews(link: str) -> dict:
```
"""

setup(
    name='detik-scrapper',
    version="1.0.6",
    description='Detik Scrapping',
    long_description=markdownData,
    long_description_content_type='text/markdown',
    author='Kiyora',
    author_email='dev@sipaling.top',
    url='https://sipaling.top',
    license='MIT',
    packages=find_packages(),
    classifiers=classifiers,
    install_requires=[
        'requests',
        'beautifulsoup4',
    ],
    keywords='detik scraping, scrapper',
)
