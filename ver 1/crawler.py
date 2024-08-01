from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from time import sleep
from bs4 import BeautifulSoup


class ManageCrawler():
    def __init__(self, url) -> None:
        self.url = url
    
    def call_page(self):
        pass