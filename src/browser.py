from bs4 import BeautifulSoup

class Browser:

    def __init__(self, parsed_page):
        self.parsed_page = parsed_page
        
    def browse_categories(self):
        a = self.parsed_page.find('div', {'class': 'side_categories'}).find('ul', {'class':'nav nav-list'}).find('li').find('ul').find('li').find('a')
        category_url = 'http://books.toscrape.com/' + a['href']
        print(category_url)
    
    def browse_books(self):
        pass