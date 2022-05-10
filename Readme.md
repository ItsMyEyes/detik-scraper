# Detik Scrapper

## 🚀 Installation
- Install package
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

## 🔐 License

Distributed under the MIT License. See [`LICENSE`](https://github.com/ItsMyEyes/detik-scraper/blob/main/LICENSE) for more information.