from booktoscrape.parse import Parser
from booktoscrape.scrapper import Scrapper

if __name__ == "__main__":
    
    url = 'http://books.toscrape.com/'

parse_response = Parser(url)
parsed_html = parse_response.html_parser()

scrapper = Scrapper(parsed_html)
category_list = scrapper.scrap_categories()

print(category_list)



