from datetime import datetime as time

class Logs:
    def __init__(self) -> None:
        pass

    def ex(self, no, url, username: str, comments: str) -> None:
        log = f"""
"no": {no}
"url": {url}
username: {username}
comments: {comments}
Status: success
Time: {time.now()}
            """
        
        print(log)