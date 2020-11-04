from urllib.parse import urljoin
from booktoscrape.parse import Parser
from booktoscrape.scrapper import Scrapper

def main ():

    URL = 'http://books.toscrape.com/'

    parser = Parser()
    scrapper = Scrapper()

    parsed_response = parser.html_parser(URL)
    category_list = scrapper.scrap_categories(parsed_response)

    scrapper.scrap_books_in_category(category_list, parser, scrapper)

if __name__ == "__main__":

    main()