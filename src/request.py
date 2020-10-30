import requests
from parse import Parser

class Request:

    def __init__(self, url):
        self.url = url

    def request_url(self):
            response = requests.get(self.url)
            if response.ok:
                parsing_response = Parser(response)
                parsing_response.html_parser()
        #except:
            #print("Nous n'avons pas réussi à établir une connexion avec la page demandée.")

url = 'http://books.toscrape.com/'
request = Request(url)
request.request_url()