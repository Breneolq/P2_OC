import requests

class Request:

    def __init__(self):
        pass

    def request_url(self, url):
        response = requests.get(url)
        if response.ok:
            return response
            