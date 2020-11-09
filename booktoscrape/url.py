from urllib.parse import urljoin

class Url:

    def __init__(self):
        pass
    
    def add_two_url(self, link_a, link_b):
        return link_a + link_b
    
    def join_url(self, link_a, link_b):
        return urljoin(link_a, link_b)
