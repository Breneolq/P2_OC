import requests
from parse import Parser

class Request:

    def __init__(self):
        pass

    def request_url(self, url, page):
            response = requests.get(url)
            if response.ok:
                parsing_response = Parser(response)
                parsing_response.html_parser(page)
        
url = 'http://books.toscrape.com'
page = 'categories'
request_site = Request()
request_site.request_url(url, page)