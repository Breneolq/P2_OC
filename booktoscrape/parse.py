import requests

from bs4 import BeautifulSoup

class Parser:

    def __init__(self):
        pass
        
    def html_parser(self, url):

        try:
            response = requests.get(url)
        except ValueError:
            print("Nous n'avons pas réussis à nous connecter à la page")
        
        parsed_html = BeautifulSoup(response.text, features="html.parser")
        parsed_html.encoding = 'utf-8'
        return parsed_html
        