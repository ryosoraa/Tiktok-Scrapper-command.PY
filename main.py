import requests
import json
from time import sleep
from libs import Scrapper
from libs import HtmlParser
from pyquery import PyQuery
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as excpect
from selenium.webdriver.chrome.options import Options


class Main:
    def __init__(self, url: str) -> None:
        self.__url_main = url

    def main(self):
        __scraper = Scrapper(aweme_id=self.__url_main.split('/')[-1])
        __scraper.ex(path='data/comment.json')



if __name__ == '__main__':
    print('exam : https://www.tiktok.com/@freyajkt48/video/7305074556123761926')
    url = input("input url video: ")
    main = Main(url=url)
    main.main()