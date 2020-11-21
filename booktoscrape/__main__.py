from requester import Requester
from scrapper import Scrapper
import constants
import os


def main():

    URL = constants.URL
    BOOKS_IDS = constants.BOOKS_IDS

    requester = Requester()
    scrapper = Scrapper(requester, URL, BOOKS_IDS)

    requested_response = requester.html_requester(URL)
    category_list = scrapper.get_category_list(requested_response)
    
    books_in_category = scrapper.scrap_books_in_category(category_list, scrapper)


if __name__ == "__main__":

    main()
