from bs4 import BeautifulSoup
from .browser import Browser

class Parser:

    def __init__(self, response):
        self.response = response
        
    def html_parser(self, page):
        parsed_html = BeautifulSoup(self.response.text, features="html.parser")
        parsed_html.encoding = 'utf-8'
        browser = Browser(parsed_html)
        getattr(browser, "browse_" + page)()
        
        