from time import sleep
import requests
import json
from json import dumps

class Scrapper:
    def __init__(self, aweme_id: str) -> None:
        self.__api = f"https://www.tiktok.com/api/comment/list/?aid=1988&count=20&current_region=JP&aweme_id={aweme_id}"
        self.__api_reply = 'https://www.tiktok.com/api/comment/list/reply/?aid=1988&aweme_id=7170139292767882522&count=20&current_region=JP&comment_id=7310933414939820805'

    def create_api(self, cid) -> str:
        apis = self.__api_reply.split('=')
        apis[-1] = str(cid)
        return '='.join(apis)

    def extract_data(self) -> dict[str, any]:
        response = requests.get(self.__api)

        content = {
                'captions': response.json()['comments'][0]['share_info']['title'].split('#')[0],
                'url': response.json()['comments'][0]['share_info']['url'],
                'total_command': response.json()['total'],
                'hastags': ['#'+tag.replace(' ', '') for tag in response.json()['comments'][0]['share_info']['title'].split('#')[1:]],
                'comments': [{
                    'uid': comment['user']['uid'],
                    'username': comment['user']['unique_id'],
                    'nickname': comment['user']['nickname'],
                    'comment': comment['text'],
                    'reply_comment_total': comment['reply_comment_total'],
                    'reply_comment': [{
                        'username': reply['user']['unique_id'],
                        'nickname': reply['user']['nickname'],
                        'comment': reply['text']
                    } for reply in requests.get(self.create_api(cid=comment['cid'])).json()['comments'] if comment['reply_comment_total'] != 0]
            } for comment in response.json()['comments']]
            }

        return content
        


    def ex(self):
        self.extract_data()

