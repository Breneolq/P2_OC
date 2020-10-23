import requests
from parse import Parse

class Request:

    def __init__(self, url):
        self.url = url
        

    def launch_request(self):
        try:
            request = requests.get(self.url)
            if request.ok:
                response = Parse(requests)
                response.parse_html()
        except:
            print('test')