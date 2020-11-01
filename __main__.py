from booktoscrape.request import Request
from booktoscrape.parse import Parser
from booktoscrape.browser import Browser

if __name__ == "__main__":
    
    url = 'http://books.toscrape.com/'
    request_site = Request()
    response = request_site.request_url(url)

page = 'categories'

parsing_response = Parser(response)
parsed_html = parsing_response.html_parser()

browser = Browser(parsed_html)
list_category = getattr(browser, "browse_" + page)()
print(list_category)

request_categories_page = Request()
response_categories_page = request_categories_page.request_url(list_category[3])

page = 'books'
parsing_response_page = Parser(response_categories_page)
parsed_html_response_page = parsing_response_page.html_parser()

browser_books = Browser(parsed_html_response_page)

list_book = getattr(browser_books, "browse_" + page)()

print(list_book)
