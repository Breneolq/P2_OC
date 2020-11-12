from bs4 import BeautifulSoup
import csv

class Scrapper:
 
    def __init__(self, parser, URL, list_of_books_ids, url):
        self.__parser = parser
        self.base_url = URL
        self.books_ids_search = list_of_books_ids
        self.__url = url

    def create_soup(self, url):
        return self.__parser.html_parser(url)
        
    def scrap_categories(self, parsed_page):
        category_list = []
        tab_of_li = parsed_page.find('ul', {'class': 'nav nav-list'}).find('li').find('ul').find_all('li')
        for li in tab_of_li:
            link = li.find('a')['href']
            category_url = self.__url.add_two_url(self.base_url, link)
            category_list.append(category_url)
        return category_list

    def scrap_books(self, parsed_page):
        list_book = []
        tab_of_li = parsed_page.find_all('li', {'class':'col-xs-6 col-sm-4 col-md-3 col-lg-3'})
        start_link = 'http://books.toscrape.com/catalogue/'
        for li in tab_of_li:
            end_link = li.find('article', {'class':'product_pod'}).find('div', {'class':'image_container'}).find('a')['href']
            end_link_short = end_link[9:]
            link = self.__url.join_url(start_link, end_link_short)
            list_book.append(link)
       
        return list_book
    
    def scrap_books_in_category(self, category_list, scrapper):
        i = 0
        while i < len(category_list):
            
            category_html = scrapper.create_soup(category_list[i])
            book_in_page_1 = scrapper.scrap_books(category_html)

            while category_html.find('li', {'class':'next'}):
                next_page = category_html.find('li', {'class': 'next'}).find('a')['href']
                category_url_next_page = self.__url.join_url(category_list[i], next_page)
                next_page_html = scrapper.create_soup(category_url_next_page)
                books_in_page = scrapper.scrap_books(next_page_html)
                book_in_page_1 = book_in_page_1 + books_in_page
                category_html = next_page_html
            scrapper.books_url(book_in_page_1, scrapper)
            
            i += 1
    
    def books_url(self, book_list, scrapper):
        for book in book_list:
            book_html = scrapper.create_soup(book)
            title = scrapper.scrap_book_title(book_html)
            category = scrapper.scrap_book_category(book_html)
            description = scrapper.scrap_book_description(book_html)
            book_infos = scrapper.scrap_in_board(book_html)
            universal_product_code = book_infos[0]
            price_including_tax = book_infos[1]
            price_excluding_tax = book_infos[2]
            number_available = book_infos[3]
            review_rating = book_infos[4]
            image_url = scrapper.scrap_book_image_url(book_html)
            scrapper.write_in_csv(title, category, description, universal_product_code, price_including_tax, price_excluding_tax, number_available, review_rating, image_url)
            
    def scrap_book_title(self, soup):
        return(soup.find('div', {'class': 'col-sm-6 product_main'}).find('h1').text.strip())
    
    def scrap_in_board(self, soup):
        books_infos = []
        i = 0
        while i < len(self.books_ids_search):
            for p in soup.find_all("th"):
                if p.text.strip() == self.books_ids_search[i]:
                    books_infos.append(p.find_next("td").text.strip())
                    i += 1
        return(books_infos)
                
    def scrap_book_description(self, soup):
        meta = soup.find('meta', {'name': 'description'})
        description = meta['content']
        return(description)

    def scrap_book_category(self, soup):
        category = soup.find('ul', {'class': 'breadcrumb'}).find_all(['a'])
        return(category[2].text.strip())

    def scrap_book_image_url(self, soup):
        link = soup.find('div', {'class': 'thumbnail'}).find('div', {'class': 'carousel-inner'}).find('div', {'class': 'item active'}).find('img')['src']
        return(self.__url.join_url(self.base_url, link))
    
    def write_in_csv(self, title, category, product_description, universal_product_code, price_including_tax, price_excluding_tax, number_available, review_rating, image_url):
        with open(category +'.csv', mode='a', encoding="utf-8", newline='') as csv_file:
            test_writer = csv.writer(csv_file, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            test_writer.writerow(['title', 'category', 'product_description', 'universal_product_code', 'price_including_tax', 'price_excluding_tax', 'number_available', 'review_rating', 'image_url'])
            test_writer.writerow([title, category, product_description, universal_product_code, price_including_tax, price_excluding_tax, number_available, review_rating, image_url])

        
        
    
    