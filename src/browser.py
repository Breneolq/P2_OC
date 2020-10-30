from bs4 import BeautifulSoup
import urllib.parse

class Browser:

    def __init__(self, parsed_page):
        self.parsed_page = parsed_page
        
    def browse_categories(self):
        a = self.parsed_page.find('div', {'class': 'side_categories'}).find('ul', {'class':'nav nav-list'}).find('li').find('ul').find('li').find('a')
        category_url = 'http://books.toscrape.com/' + a['href']
        print(category_url)
    
    def browse_books(self):
        a = self.parsed_page.find('article', {'class': 'product_pod'}).find('h3').find('a')
        end_link = a['href']
        start_link = 'http://books.toscrape.com/catalogue/test/test'
        link = urllib.parse.urljoin(start_link, end_link)
        print(link)