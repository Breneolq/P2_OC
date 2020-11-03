import urllib.parse
from booktoscrape.parse import Parser
from booktoscrape.scrapper import Scrapper

if __name__ == "__main__":
    
    url = 'http://books.toscrape.com/'

#Test méthode de récupération URL des catégories

parse_response = Parser()
scrapper = Scrapper()

parsed_response = parse_response.html_parser(url)
category_list = scrapper.scrap_categories(parsed_response)

#Test méthode de récupération URL de la page suivante
"""
category_html = parse_response.html_parser(list_category[3])

books_in_category = scrapper.scrap_books(category_html)
"""
#Test méthode de récupération Url des livres sur la page
"""
book_response = Parser(list_category[0])
book_response_parsed = book_response.html_parser()

book_url_scrapper = Scrapper(book_response_parsed)
book_url_list = book_url_scrapper.scrap_books()
"""
print(category_list)




