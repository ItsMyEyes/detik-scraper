import requests
from bs4 import BeautifulSoup

#list standar news
def listCategory():
    urlCategory = "https://news.detik.com"
    data = requests.get(urlCategory)
    soup = BeautifulSoup(data.text, 'html.parser')
    listCategory = soup.find('ul', class_='nav--column-2').find_all('a')
    list_kamu = list()
    for i in listCategory:
        title = i.text.strip()
        link = i.get('href')
        list_kamu.append({'title': title, 'link': link})
    return list_kamu

def ListNews(category):
    data = listCategory()
    for i in data:
        if i['title'].upper() == category.upper():
            data = requests.get(i['link'])
            soup = BeautifulSoup(data.text, 'html.parser')
            list_news = soup.find('div', class_='list-content').find_all('article', class_='list-content__item')
            list_aku = list()
            for i in list_news:
                link = i.find('a').get('href')
                title = i.find('a').get('dtr-ttl')
                list_aku.append({'link': link, 'title': title})
            return list_aku
    return { "code": 404, "message": "category not found" }

# ListHot
def HotNewsList():
    urlDetikHot = "https://hot.detik.com/"
    data = requests.get(urlDetikHot)
    soup = BeautifulSoup(data.text, 'html.parser')
    hotNews = soup.find('div', class_='cb-mostpop')
    ini = hotNews.find_all('a', attrs={'dtr-act': 'terpopuler'})
    key  = 0
    hot = list()
    for i in ini:
        key += 1
        title = i.text.strip()
        link = i.get('href')
        hot.append({'number_news': key,'title': title, 'link': link})
    return hot

# # Detail
def DetailNews(link):
    data = requests.get(link)
    soup = BeautifulSoup(data.text, 'html.parser')
    article = soup.find('article', class_='detail')
    title = article.find('h1', class_='detail__title').text.strip()
    if title == '':
        return { 'code': 404, 'message': 'Not Found' }
    
    date = article.find('div', class_='detail__date').text.strip()

    desc = article.find('div', class_='detail__body-text')
    detail_dec = desc.find_all('p')
    detail = list()
    for i in detail_dec:
        detail.append(i.text.strip())   

    tag_fol = article.find_all('a', attrs={'dtr-act': 'tag'})
    tag = list()
    for i in tag_fol:
        tag.append(i.text.strip())
    return {'title': title, 'date': date, 'detail': detail, 'tag': tag}