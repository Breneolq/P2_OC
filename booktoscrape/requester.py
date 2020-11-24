import requests
from bs4 import BeautifulSoup

class RequesterException(Exception):
    pass

class Requester:

    def __init__(self):
        pass

    def html_requester(self, url): #Fait une requete et retourne une réponse encodé en UTF-8 afin de pouvoir facilement récuperer des informations
        response = requests.get(url)

        if response.status_code != 200:
            raise RequesterException(f"Impossible de recuperer la page {url}, error {response.status_code}")    
        
        request_html = BeautifulSoup(response.content.decode('utf-8', 'ignore'), features="html.parser")
        request_html.encode("utf8")
        return request_html
