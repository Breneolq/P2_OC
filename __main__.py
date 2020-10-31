from booktoscrape import request

if __name__ == "__main__":
    url = 'http://books.toscrape.com/catalogue/category/books/fiction_10/index.html'
    page = 'books'
    request_site = Request()
    request_site.request_url(url, page)
