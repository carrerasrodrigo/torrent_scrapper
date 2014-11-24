import requests
from bs4 import BeautifulSoup


class Browser:

    def __init__(self):
        self.session = requests.Session()

    def get(self, url, params=None):
        f = self.session.get(url, params=params)
        return f.content

    def post(self, url, params=None):
        pass

    def get_soup(self, url, data=None):
        return BeautifulSoup(self.get(url, data))

    def post_soup(self, url, data=None):
        return BeautifulSoup(self.post(url, data))
