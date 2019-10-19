import requests


class NewsEngine:
    def __init__(self, topic, pageSize, NEWS_API_KEY):
        self.topic = topic
        self.pageSize = str(pageSize)
        self.NEWS_API_KEY = NEWS_API_KEY

    def fetchNews(self):
        url = "https://newsapi.org/v2/everything?q=" + self.topic + "&apiKey=" + self.NEWS_API_KEY + "&pageSize=" + self.pageSize
        r = requests.get(url=url)
        data = r.json()  # extracting data in json format

        ## Formating data to be returned
        data = data['articles']
        return data