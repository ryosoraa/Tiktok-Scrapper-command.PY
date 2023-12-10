import requests
import json
from pyquery import PyQuery
from libs.utils.parser import HtmlParser

class Scrapper:
    def __init__(self) -> None:
        self.__parser = PyQuery()
        self.__api = 'https://www.tiktok.com/api/comment/list/?WebIdLastTime=1702206311&aid=1988&app_language=ja-JP&app_name=tiktok_web&aweme_id=7170139292767882522&browser_language=id&browser_name=Mozilla&browser_online=true&browser_platform=Win32&browser_version=5.0 (Windows)&channel=tiktok_web&cookie_enabled=true&count=20&current_region=JP&cursor=0&device_id=7310920380687025682&device_platform=web_pc&enter_from=tiktok_web&focus_state=true&fromWeb=1&from_page=video&history_len=6&is_fullscreen=false&is_non_personalized=false&is_page_visible=true&os=windows&priority_region=&referer=&region=ID&root_referer=https://www.google.com/&screen_height=1080&screen_width=1920&tz_name=Asia/Jakarta&verifyFp=verify_lpzdpjp3_TwahSIGy_2yrZ_4BVq_BHxe_soMok4JmM93R&webcast_language=id-ID&msToken=Tt6BhEJ8oFCJMm0tPlQWz36tG-sCTqg49Yt65laVyS011Q5-DMH28smioMMk8Y-pgsCPbe3of-kByoRzETsxxVXz-IPV7-FEy20z5mbUqPHaeDXQJ46tcccS8g==&X-Bogus=DFSzsIVO7RJANj6qtuhRDU9WcBjv&_signature=_02B4Z6wo00001nUrvAAAAIDCdSu8A6lfv5Z1KbiAAPhOef'

    
    def extract_data(self, url: str):
        response = requests.get(self.__api)
        
        
        pass


    def ex(self):
        pass
