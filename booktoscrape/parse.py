from bs4 import BeautifulSoup

class Parser:

    def __init__(self, response):
        self.response = response
        
    def html_parser(self):
        parsed_html = BeautifulSoup(self.response.text, features="html.parser")
        parsed_html.encoding = 'utf-8'
        return parsed_html
        