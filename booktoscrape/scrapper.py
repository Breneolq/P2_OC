from pathlib import Path
from urllib.parse import urljoin
from urllib.request import urlretrieve
import requests
import shutil

import os
import csv

import constants


class Scrapper:
    def __init__(self, requester):
        self.requester = requester

    def create_soup(self, url):
        """
        Recupère le contenu d'une page HTML
        """
        return self.requester.html_requester(url)

    def get_category_list(self, requested_page):
        """
        Récupère la liste des urls des catégories
        """
        os.chdir("./booktoscrape/results")
        category_list = []
        tab_of_li = (
            requested_page.find("ul", {"class": "nav nav-list"})
            .find("li")
            .find("ul")
            .find_all("li")
        )
        for li in tab_of_li:
            link = li.find("a")["href"]
            category_url = urljoin(constants.URL, link)
            category_list.append(category_url)
        return category_list

    def scrap_books_in_category(self, category_list, scrapper):
        """
        Récupère toutes les URL des livres de la catégorie
        """

        for category in category_list:

            category_html = scrapper.create_soup(category)
            book_in_page_1 = scrapper.scrap_books(category_html)

            while category_html.find("li", {"class": "next"}):
                next_page = category_html.find("li", {"class": "next"}).find("a")[
                    "href"
                ]
                category_url_next_page = urljoin(category, next_page)
                next_page_html = scrapper.create_soup(category_url_next_page)
                books_in_page = scrapper.scrap_books(next_page_html)
                book_in_page_1 = book_in_page_1 + books_in_page
                category_html = next_page_html
            scrapper.write_book(book_in_page_1, scrapper)

    def scrap_books(self, requested_page):
        """
        Récupère les URL des livres de la première page de la catégorie
        """
        list_book = []
        tab_of_li = requested_page.find_all(
            "li", {"class": "col-xs-6 col-sm-4 col-md-3 col-lg-3"}
        )
        start_link = "http://books.toscrape.com/catalogue/"
        for li in tab_of_li:
            end_link = (
                li.find("article", {"class": "product_pod"})
                .find("div", {"class": "image_container"})
                .find("a")["href"]
            )
            end_link_short = end_link[9:]
            link = urljoin(start_link, end_link_short)
            list_book.append(link)

        return list_book

    def write_book(self, book_list, scrapper):
        """
        Lance la récupération de toutes les informations necessaire des livres, puis écrit dans dans un fichier CSV
        """
        for book in book_list:
            book_html = scrapper.create_soup(book)
            title = scrapper.scrap_book_title(book_html)
            category = scrapper.scrap_book_category(book_html)
            description = scrapper.scrap_book_description(book_html)
            book_infos = scrapper.scrap_in_board(book_html)
            universal_product_code = book_infos[0]
            price_including_tax = book_infos[1]
            price_excluding_tax = book_infos[2]
            number_available = book_infos[3]
            review_rating = scrapper.scrap_stars_of_review(book_html)
            image_url = scrapper.scrap_book_image_url(book_html)
            scrapper.write_in_csv(
                title,
                category,
                description,
                universal_product_code,
                price_including_tax,
                price_excluding_tax,
                number_available,
                review_rating,
                image_url,
            )
            r = requests.get(image_url, stream=True)

            if r.status_code == 200:
                r.raw.decode_content = True

                with open(title, "wb") as f:
                    shutil.copyfileobj(r.raw, f)
            else:
                print("Image Couldn't be retreived")
            # urlretrieve(image_url, title + ".jpg")

    def scrap_stars_of_review(self, soup):
        """
        Récupère le nombre d'étoile
        """
        classe = str(soup.find("p", {"class": "star-rating"})["class"])
        if classe == "['star-rating', 'One']":
            return 1
        elif classe == "['star-rating', 'Two']":
            return 2
        elif classe == "['star-rating', 'Three']":
            return 3
        elif classe == "['star-rating', 'Four']":
            return 4
        elif classe == "['star-rating', 'Five']":
            return 5

    def scrap_book_title(self, soup):
        """
        Récupère le titre
        """
        title = (
            soup.find("div", {"class": "col-sm-6 product_main"}).find("h1").text.strip()
        )
        for char in title:
            if char in " ?.!/;:,#()%":
                title = title.replace(char, " ")
        return title

    def scrap_in_board(self, soup):
        """
        Récupère le tableau avec les informations de type, price_including_tax et excluding_tax, l'upc...
        """
        books_infos = []
        for ids in constants.BOOKS_IDS:
            for p in soup.find_all("th"):
                if p.text.strip() == ids:
                    books_infos.append(p.find_next("td").text.strip())
        return books_infos

    def scrap_book_description(self, soup):
        """
        Récupère la description du livre
        """
        meta = soup.find("meta", {"name": "description"})
        description = meta["content"]
        return description

    def scrap_book_category(self, soup):
        """
        Récupère le om de la catégorie
        """
        category = soup.find("ul", {"class": "breadcrumb"}).find_all(["a"])
        return category[2].text.strip()

    def scrap_book_image_url(self, soup):
        """
        Récupère l'url de l'image
        """
        link = (
            soup.find("div", {"class": "thumbnail"})
            .find("div", {"class": "carousel-inner"})
            .find("div", {"class": "item active"})
            .find("img")["src"]
        )
        return urljoin(constants.URL, link)

    def write_in_csv(
        self,
        title,
        category,
        product_description,
        universal_product_code,
        price_including_tax,
        price_excluding_tax,
        number_available,
        review_rating,
        image_url,
    ):
        """
        Ecrit en les informations dans un fichier CSV
        """
        with Path(category + ".csv").open("a", encoding="utf-8") as csv_file:
            test_writer = csv.writer(
                csv_file, delimiter=";", quotechar='"', quoting=csv.QUOTE_MINIMAL
            )
            test_writer.writerow(constants.CSV_INDEX)
            test_writer.writerow(
                [
                    title,
                    category,
                    product_description,
                    universal_product_code,
                    price_including_tax,
                    price_excluding_tax,
                    number_available,
                    review_rating,
                    image_url,
                ]
            )
        return
