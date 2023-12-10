from time import sleep
import requests
import json
from json import dumps
from pyquery import PyQuery
from libs.utils.parser import HtmlParser
from libs.utils.Writers import Writer

class Scrapper:
    def __init__(self) -> None:
        self.__api = "https://www.tiktok.com/api/comment/list/?aid=1988&aweme_id=7170139292767882522&count=20&current_region=JP"
        self.__api_reply = 'https://www.tiktok.com/api/comment/list/reply/?aid=1988&aweme_id=7170139292767882522&count=20&current_region=JP&comment_id=7310933414939820805'

    def create_api(self, cid) -> str:
        apis = self.__api_reply.split('=')
        apis[-1] = str(cid)
        print(apis)
        return '='.join(apis)

    def extract_data(self):
        response = requests.get(self.__api)
        

        print(response.json()['total'])

        content = {
                'desc': response.json()['comments'][0]['share_info']['title'].split('#')[0],
                'url': response.json()['comments'][0]['share_info']['url'],
                'total_command': response.json()['total'],
                'hastags': ['#'+tag.replace(' ', '') for tag in response.json()['comments'][0]['share_info']['title'].split('#')[1:]],
                'comments': []
            }

        for comment in response.json()['comments']:
            comments = {
                'uid': comment['user']['uid'],
                'username': comment['user']['unique_id'],
                'nickname': comment['user']['nickname'],
                'comment': comment['text'],
                'reply_comment_total': comment['reply_comment_total'],
                'reply_comment': []
            }


            if comment['reply_comment_total'] != 0:
                response_reply = requests.get(self.create_api(cid=comment['cid']))

                for reply in response_reply.json()['comments']:

                    print(comment['user']['unique_id'])
                    print(comment['user']['unique_id'])

                    comments['reply_comment'].append(
                        {
                            'username': reply['user']['unique_id'],
                            'nickname': reply['user']['nickname'],
                            'comment': reply['text']
                        } 
                    )
            content['comments'].append(comments)

            print(comments)
            sleep(3)
            print('\n')
        with open('private/results2.json', 'w', encoding="utf-8") as file:
            json.dump(content, file, indent=2, ensure_ascii=False)
        


    def ex(self):
        pass

