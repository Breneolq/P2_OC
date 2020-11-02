import urllib.parse
from booktoscrape.parse import Parser
from booktoscrape.scrapper import Scrapper

if __name__ == "__main__":
    
    url = 'http://books.toscrape.com/'

parse_response = Parser(url)
parsed_html = parse_response.html_parser()

scrapper = Scrapper(parsed_html)
category_list = scrapper.scrap_categories()

i = 0

while i < len(category_list):
    category_response = Parser(category_list[i])
    i += 1
    category_html = category_response.html_parser()

    category_scrapper = Scrapper(category_html)

    book_list = category_scrapper.scrap_books()

    print(book_list)




