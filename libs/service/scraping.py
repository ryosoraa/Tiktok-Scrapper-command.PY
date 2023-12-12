from time import sleep
import requests
import json
from json import dumps
from libs.utils.Writers import Writer
from libs.utils.logs import Logs

class Scrapper:
    def __init__(self, aweme_id: str) -> None:
        self.__api = f"https://www.tiktok.com/api/comment/list/?aid=1988&current_region=JP&aweme_id={aweme_id}&count=50&cursor=0"
        self.__api_reply = 'https://www.tiktok.com/api/comment/list/reply/?aid=1988&current_region=JP&count=50&cursor=0&comment_id=7305177451981849350'
        self.__results = []
        self.__writer = Writer()
        self.__logs = Logs()

    def create_api(self, url, cursor) -> str:
        apis = url.split('&')
        apis[-1] = str(f'cursor={cursor}')

        return '&'.join(apis)


    def create_api_reply(self, url_api, command_id, cursor) -> str:
        apis = url_api.split('&')
        apis[-1] = str(f'comment_id={command_id}')
        apis[-2] = str(f'cursor={cursor}')
        
        return '&'.join(apis)


    def extract_data(self, path: str) -> dict[str, any]:
        try:
            response = requests.get(self.__api)
        except:
            print('error')
        content = {
                'captions': response.json()['comments'][0]['share_info']['title'].split('#')[0],
                'url': response.json()['comments'][0]['share_info']['url'],
                'total_command': response.json()['total'],
                'hastags': ['#'+tag.replace(' ', '') for tag in response.json()['comments'][0]['share_info']['title'].split('#')[1:]],
                'comments': [] 
            }

        cursor_main = 0
        id_comment = 1
        page = 100
        while True:
            main_url = self.create_api(url=self.__api, cursor=cursor_main)
            cursor_main+=50
            try:
                response = requests.get(main_url)          
            except:
                print("error")

            if response.json()['comments'] == None: break
            for comment in response.json()['comments']:

                self.__logs.ex(no=id_comment, url=main_url,comments=comment['text'], username=comment['user']['unique_id'])

                comments = {
                  'uid': comment['user']['uid'],
                  'username': comment['user']['unique_id'],
                  'nickname': comment['user']['nickname'],
                  'comment': comment['text'],
                  'reply_comment_total': comment['reply_comment_total'],
                  'reply_comment': []
                }
                
                if comment['reply_comment_total'] != 0:

                    cursor_reply = 0
                    while True:
                        url = self.create_api_reply(url_api=self.__api_reply, command_id=comment['cid'], cursor=cursor_reply)
                        cursor_reply+=50

                        try:
                            response = requests.get(url=url)
                        except:
                            print('error')

                        if response.json()['total'] == 0: break
                        for reply in response.json()['comments']:

                            try:
                                comments['reply_comment'].append({
                                                'username': reply['user']['unique_id'],
                                                'nickname': reply['user']['nickname'],
                                                'comment': reply['text']
                                                })
                            except:
                                comments['reply_comment'].append({})

                content['comments'].append(comments)
                id_comment+=1

                if len(content['comments']) == page: self.__writer.ex(path=f'data/page/{page}.json', content=content); page+=100; 


        self.__writer.ex(path=path, content=content)
        


    def ex(self, path: str):
        self.extract_data(path=path)

