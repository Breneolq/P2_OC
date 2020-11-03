import urllib.parse
from booktoscrape.parse import Parser
from booktoscrape.scrapper import Scrapper

if __name__ == "__main__":
    
    url = 'http://books.toscrape.com/'

#Test méthode de récupération URL des catégories

parse_response = Parser(url)
parsed_response = parse_response.html_parser()

scrapper = Scrapper(parsed_response)
list_category = scrapper.scrap_categories()

#Test méthode de récupération URL de la page suivante
"""
category_response = Parser(list_category[3])
category_html = category_response.html_parser()

category_scrapper = Scrapper(category_html)
category_url_next_page = category_scrapper.scrap_page_in_categories(list_category[3])
"""
#Test méthode de récupération Url des livres sur la page
"""
book_response = Parser(list_category[0])
book_response_parsed = book_response.html_parser()

book_url_scrapper = Scrapper(book_response_parsed)
book_url_list = book_url_scrapper.scrap_books()
"""
print(list_category)




