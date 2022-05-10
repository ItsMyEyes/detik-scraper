<p align="center">

  <h3 align="center">Detik Scraper</h3>

  <p align="center">
    Detik scrapper
    <br />
    <br />
    <a href="https://github.com/ItsMyEyes/detik-scraper/issues">Report Bug</a>
    ·
    <a href="https://github.com/ItsMyEyes/detik-scraper/issues">Request Feature</a>
  </p>
</p>

## 📎 Requirements
* requests
* BeautifulSoup


## 🚀 Installation
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

## 🔐 License

Distributed under the MIT License. See [`LICENSE`](https://github.com/ItsMyEyes/detik-scraper/blob/master/LICENSE) for more information.