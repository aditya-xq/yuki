import requests


class NewsEngine:
    def __init__(self, pageSize, NEWS_API_KEY):
        self.pageSize = str(pageSize)
        self.NEWS_API_KEY = NEWS_API_KEY

    def fetchNews(self, topic):
        url = "https://newsapi.org/v2/everything?q=" + topic + "&apiKey=" + self.NEWS_API_KEY + "&pageSize=" + self.pageSize
        r = requests.get(url=url)
        data = r.json()  # extracting data in json format

        ## Formating data to be returned
        data = data['articles']
        return data