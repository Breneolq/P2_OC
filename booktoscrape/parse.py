import requests

from bs4 import BeautifulSoup

class Parser:

    def __init__(self, url):
        self.url = url
        
    def html_parser(self):
        response = requests.get(self.url)
        parsed_html = BeautifulSoup(response.text, features="html.parser")
        parsed_html.encoding = 'utf-8'
        return parsed_html
        