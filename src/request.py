import requests
from parse import Parser

class Request:

    def __init__(self):
        pass

    def request_url(self, url):
            response = requests.get(url)
            if response.ok:
                parsing_response = Parser(response)
                parsing_response.html_parser()
        
url = 'http://books.toscrape.com/catalogue/category/books/travel_2/index.html'
request_site = Request()
request_site.request_url(url)