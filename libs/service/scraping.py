from time import sleep
import requests
import json
from json import dumps
from pyquery import PyQuery
from libs.utils.parser import HtmlParser
from libs.utils.Writers import Writer

class Scrapper:
    def __init__(self) -> None:
        # self.__parser = PyQuery()
        self.__api = "https://www.tiktok.com/api/comment/list/?aid=1988&aweme_id=7170139292767882522&channel=tiktok_web&cookie_enabled=true&count=20&cursor=0&enter_from=tiktok_web&focus_state=true&fromWeb=1&msToken=Tt6BhEJ8oFCJMm0tPlQWz36tG-sCTqg49Yt65laVyS011Q5-DMH28smioMMk8Y-pgsCPbe3of-kByoRzETsxxVXz-IPV7-FEy20z5mbUqPHaeDXQJ46tcccS8g==&X-Bogus=DFSzsIVO7RJANj6qtuhRDU9WcBjv&_signature=_02B4Z6wo00001nUrvAAAAIDCdSu8A6lfv5Z1KbiAAPhOef"
    
    def extract_data(self):
        response = requests.get(self.__api)

        print(response.json()['total'])

        content = {
                'desc': response.json()['comments'][0]['share_info']['title'].split('#')[0],
                'url': response.json()['comments'][0]['share_info']['url'],
                'total_command': response.json()['total'],
                'hastags': ['#'+tag.replace(' ', '') for tag in response.json()['comments'][0]['share_info']['title'].split('#')[1:]]
            }

        print(content)
        # for command in response.json()['comments']:
        #     print(command['user']['nickname'])


        #     result = {
        #         'uid': command['user']['uid'],
        #         'unique_id': command['user']['unique_id'],
        #         'nickname': command['user']['nickname'],
        #     }
        #     # print(command)
        #     sleep(2)


        # with open('private/test.json', 'w', encoding="utf-8") as file:
        #     json.dump(response.json(), file, indent=2, ensure_ascii=False)
        


    def ex(self):
        pass

