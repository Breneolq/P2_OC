import requests

from bs4 import BeautifulSoup

class Parser:

    def __init__(self, url):
        self.url = url
        
    def html_parser(self):

        try:
            response = requests.get(self.url)
        except ValueError:
            print("Nous n'avons pas réussis à nous connecter à la page")
        
        parsed_html = BeautifulSoup(response.text, features="html.parser")
        parsed_html.encoding = 'utf-8'
        return parsed_html
        