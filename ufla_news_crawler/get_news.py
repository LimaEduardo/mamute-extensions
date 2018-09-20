import requests
import json
from bs4 import BeautifulSoup

def get_news():
    url = 'https://ufla.br/noticias'

    page_content = requests.get(url).content

    soup = BeautifulSoup(page_content)

    number_of_news = 5
    news = []

    body = soup.find("body")
    for i in range(number_of_news):
        image = body.find_next("img", {"class": "img-rounded"})
        subtitle = image.find_next("div", {"class": "subtitle"})
        title = subtitle.find_next("a")
        trash = title.find_next("li")
        date = trash.find_next("li")
        hour = date.find_next("li")

        data = {
            "image_url" : str.strip(image['src']),
            "subtitle" : str.strip(subtitle.string),
            "title" : str.strip(title.string),
            "date" : str.strip(date.text),
            "hour" : str.strip(hour.text)
        }

        news.append(data)
        
        body = hour

    return json.dumps(news)

