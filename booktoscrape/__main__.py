from requester import Requester
from scrapper import Scrapper
import constants


def main():
    """
    Instancie mes classes Requester et Scrapper, effectue une première requete puis transmet la réponse au scrapper
    """

    requester = Requester()
    scrapper = Scrapper(requester)

    requested_response = requester.html_requester(constants.URL)
    category_list = scrapper.get_category_list(requested_response)

    scrapper.scrap_books_in_category(category_list, scrapper)


if __name__ == "__main__":

    main()
