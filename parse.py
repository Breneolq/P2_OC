from bs4 import BeautifulSoup

class Parse:

    def __init__(self, response):
        self.response = response
    
    def parse_html(self):
        parse = BeautifulSoup(self.response + '.text', features="html.parser")
        parse.encoding = 'utf-8'
