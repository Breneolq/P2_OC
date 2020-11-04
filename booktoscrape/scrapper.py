from bs4 import BeautifulSoup

from urllib.parse import urljoin

class Scrapper:
    
    url_list = []
 
    def __init__(self):
        pass
        
    def scrap_categories(self, parsed_page):
        category_list = []
        tab_of_li = parsed_page.find('ul', {'class': 'nav nav-list'}).find('li').find('ul').find_all('li')
        for li in tab_of_li:
            a = li.find('a')
            link = a['href']
            category_url = 'http://books.toscrape.com/' + link
            category_list.append(category_url)
        return category_list

    def scrap_books(self, parsed_page):
        list_book = []
        tab_of_li = parsed_page.find_all('li', {'class':'col-xs-6 col-sm-4 col-md-3 col-lg-3'})
        for li in tab_of_li:
            a = li.find('article', {'class':'product_pod'}).find('div', {'class':'image_container'}).find('a')
            end_link = a['href']
            end_link_short = end_link[9:]
            start_link = 'http://books.toscrape.com/catalogue/'
            link = urljoin(start_link, end_link_short)
            list_book.append(link)
       
        return list_book
    
    def scrap_books_in_category(self, category_list, parser, scrapper):
        i = 0
        while i < len(category_list):

            category_html = parser.html_parser(category_list[i])
            book_in_page_1 = scrapper.scrap_books(category_html)

            while category_html.find('li', {'class':'next'}):
                a = category_html.find('li', {'class': 'next'}).find('a')
                next_page = a['href']
                category_url_next_page = urljoin(category_list[i], next_page)
                next_page_html = parser.html_parser(category_url_next_page)
                books_in_page = scrapper.scrap_books(next_page_html)
                book_in_page_1 = book_in_page_1 + books_in_page
                category_html = next_page_html
            i += 1
        
        
    
    