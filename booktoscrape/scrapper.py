from bs4 import BeautifulSoup

from urllib.parse import urljoin

class Scrapper:
 
    def __init__(self, parsed_page):
        self.parsed_page = parsed_page
        
    def scrap_categories(self):
        list_category = []
        tab_of_li = self.parsed_page.find('ul', {'class': 'nav nav-list'}).find('li').find('ul').find_all('li')
        for li in tab_of_li:
            a = li.find('a')
            link = a['href']
            category_url = 'http://books.toscrape.com/' + link
            list_category.append(category_url)
        return list_category
    
    def scrap_page_in_categories(self, category_url):
        if self.parsed_page.find('li', {'class':'next'}):
            a = self.parsed_page.find('li', {'class': 'next'}).find('a')
            next_page = a['href']
            category_url_next_page = urljoin(category_url, next_page)
            return category_url_next_page
        else :
            pass
    
    def scrap_books(self):
        list_book = []
        tab_of_li = self.parsed_page.find_all('li', {'class':'col-xs-6 col-sm-4 col-md-3 col-lg-3'})
        for li in tab_of_li:
            a = li.find('article', {'class':'product_pod'}).find('div', {'class':'image_container'}).find('a')
            end_link = a['href']
            end_link_short = end_link[9:]
            start_link = 'http://books.toscrape.com/catalogue/'
            link = start_link + end_link_short
            list_book.append(link)
        return list_book
        
    
    