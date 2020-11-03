from urllib.parse import urljoin
from booktoscrape.parse import Parser
from booktoscrape.scrapper import Scrapper

if __name__ == "__main__":
    
    url = 'http://books.toscrape.com/'

#Test méthode de récupération URL des catégories

parser = Parser()
scrapper = Scrapper()

parsed_response = parser.html_parser(url)
category_list = scrapper.scrap_categories(parsed_response)

#test pagination
i = 3

if i == 3:
    
    category_html = parser.html_parser(category_list[i])
    book_in_page_1 = scrapper.scrap_books(category_html)
    
    while category_html.find('li', {'class':'next'}):
        a = category_html.find('li', {'class': 'next'}).find('a')
        next_page = a['href']
        category_url_next_page = urljoin(category_list[i], next_page)
        next_page_html = parser.html_parser(category_url_next_page)
        books_in_page = scrapper.scrap_books(next_page_html)
        books = book_in_page_1 + books_in_page
        category_html = next_page_html
        print(books)

#Test méthode de récupération URL de la page suivante
"""
category_html = parse_response.html_parser(list_category[3])

books_in_category = scrapper.scrap_page_in_categories(category_html)
"""
#Test méthode de récupération Url des livres sur la page
"""
book_response = Parser(list_category[0])
book_response_parsed = book_response.html_parser()

book_url_scrapper = Scrapper(book_response_parsed)
book_url_list = book_url_scrapper.scrap_books()
"""





