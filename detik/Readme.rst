# Detik Scrapper

## Requirements
* requests
* BeautifulSoup


## Installation
- Clone Repository (name must detik!!!)
```
$ git clone https://github.com/ItsMyEyes/detik-scraper.git detik
```
- Install package
After cloning, go to directory and run this command for installation package
```
$ pip install request
$ pip install beautifulsoup4
```
- Then you test it with new file like main.py / Example Code
```
import detik
import json

print(json.dumps(detik.getListHotNews(), indent=4))
```