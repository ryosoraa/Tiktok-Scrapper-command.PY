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
        self.__api_reply = 'https://www.tiktok.com/api/comment/list/reply/?WebIdLastTime=1702206311&aid=1988&app_language=ja-JP&app_name=tiktok_web&browser_language=id&browser_name=Mozilla&browser_online=true&browser_platform=Win32&browser_version=5.0%20%28Windows%29&channel=tiktok_web&comment_id=7310933414939820805&cookie_enabled=true&count=3&current_region=JP&cursor=0&device_id=7310920380687025682&device_platform=web_pc&enter_from=tiktok_web&focus_state=true&fromWeb=1&from_page=video&history_len=6&is_fullscreen=false&is_page_visible=true&item_id=7170139292767882522&os=windows&priority_region=&referer=&region=ID&root_referer=https%3A%2F%2Fwww.google.com%2F&screen_height=1080&screen_width=1920&tz_name=Asia%2FJakarta&verifyFp=verify_lpzdpjp3_TwahSIGy_2yrZ_4BVq_BHxe_soMok4JmM93R&webcast_language=id-ID&msToken=2_BaEneCNSga5qd63-6TqRxlPg0VqPo7TSuHsEhH83vqcrFOk6rEtloyaNctTJBPMr6ezlOsQo6w2FRL5pjkN9k_4CLXozsTiOJ8phKYwkayfwRp_36vsIXLrw==&X-Bogus=DFSzsIVYO5TANyKituglpU9WcBjl&_signature=_02B4Z6wo00001PwppVwAAIDA.CmlXalK..j8K6HAAFqFbc'
    def extract_data(self):
        response = requests.get(self.__api)
        response_reply = requests.get(self.__api_reply)

        print(response.json()['total'])

        content = {
                'desc': response.json()['comments'][0]['share_info']['title'].split('#')[0],
                'url': response.json()['comments'][0]['share_info']['url'],
                'total_command': response.json()['total'],
                'hastags': ['#'+tag.replace(' ', '') for tag in response.json()['comments'][0]['share_info']['title'].split('#')[1:]],
                'comments': []
            }

        for ind, comment in enumerate(response.json()['comments']):
            comments = {
                'uid': comment['user']['uid'],
                'username': comment['user']['unique_id'],
                'nickname': comment['user']['nickname'],
                'comment': comment['text'],
                'reply_comment_total': comment['reply_comment_total'],
                'reply_comment': []
            }

            if comment['reply_comment'] != None:
                print(len(comment['reply_comment']))

                for reply in response_reply.json()['comments']:
                    print(reply)
                    print(reply['reply_id'])
                    print(comment['reply_id'])
                    if reply['reply_id'] == comment['reply_id']:

                        comments['reply_comment'].append(
                            {
                                'username': reply['user']['unique_id'],
                                'nickname': reply['user']['nickname'],
                                'comment': reply['text']
                            }
                        )
            content['comments'].append(comments)


        with open('private/results2.json', 'w', encoding="utf-8") as file:
            json.dump(content, file, indent=2, ensure_ascii=False)
        


    def ex(self):
        pass

