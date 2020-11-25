from requester import Requester
from scrapper import Scrapper
import constants


def main():
    """
    Défini mes constantes, Instancie mes classes Requester et Scrapper, effectue une première requete puis transmet la réponse au scrapper
    """
    URL = constants.URL
    BOOKS_IDS = constants.BOOKS_IDS

    requester = Requester()
    scrapper = Scrapper(requester, URL, BOOKS_IDS)

    requested_response = requester.html_requester(URL)
    category_list = scrapper.get_category_list(requested_response)

    scrapper.scrap_books_in_category(category_list, scrapper)


if __name__ == "__main__":

    main()
