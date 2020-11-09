from booktoscrape.url import Url
from booktoscrape.parse import Parser
from booktoscrape.scrapper import Scrapper

def main ():

    URL = 'http://books.toscrape.com/'
    BOOKS_IDS = ['UPC', 'Price (incl. tax)', 'Price (excl. tax)', 'Availability', 'Number of reviews']

    url = Url()
    parser = Parser()
    scrapper = Scrapper(parser, URL, BOOKS_IDS, url)
    

    parsed_response = parser.html_parser(URL)
    category_list = scrapper.scrap_categories(parsed_response)

    scrapper.scrap_books_in_category(category_list, scrapper)

if __name__ == "__main__":

    main()