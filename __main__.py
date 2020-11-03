import urllib.parse
from booktoscrape.parse import Parser
from booktoscrape.scrapper import Scrapper

if __name__ == "__main__":
    
    url = 'http://books.toscrape.com/'

parse_response = Parser(url)
parsed_html = parse_response.html_parser()

scrapper = Scrapper(parsed_html)
list_category = scrapper.scrap_categories()

#Test méthode de récupération URL de page

category_response = Parser(list_category[3])
category_html = category_response.html_parser()

category_scrapper = Scrapper(category_html)
category_url_next_page = category_scrapper.scrap_page_in_categories(list_category[3])

print(category_url_next_page)




