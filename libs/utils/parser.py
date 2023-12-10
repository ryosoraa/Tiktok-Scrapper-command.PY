from pyquery import PyQuery

class HtmlParser:
    def __init__(self) -> None:
        pass

    def ex(self, html: PyQuery, selector: str):
        try:
            return PyQuery(html.text).find(selector=selector)
        except Exception as err:
            print(err)