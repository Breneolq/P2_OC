import csv
import requests
from bs4 import BeautifulSoup

        #Première Etape#

"""
    -Choisir une page Produit & se connecter

"""

url_produit = 'http://books.toscrape.com/catalogue/in-a-dark-dark-wood_963/index.html'
response = requests.get(url_produit)

"""
    
    -Extraire les infos:
        product_page_url
        universal_product_code
        title
        price_including_tax
        price_excluding_tax
        number_available
        product_description
        category
        review_rating
        image_url
    
"""
if response.ok:
    soup = BeautifulSoup(response.text, features="html.parser")
    product_page_url = url_produit
    universal_product_code = 0
    title = 0
    price_including_tax = 0
    price_excluding_tax = 0
    number_available = 0
    product_description = 0
    category = 0
    review_rating = 0
    image_url = 0

    print(product_page_url)


"""
    -Ecrire les données dans un fichier CSV en colonne avec
    les valeurs ci dessus comme en-tête
"""

        #Seconde Etape#

"""
    -Etendre le script afin de récupérer toutes les données d'une
    catégorie

    -Attention au passage d'une page à l'autre
"""

        #Troisième Etape#

"""
    -Parcourir toutes les catégories et récupérer les infos
    de tous les produits dans autant de fichiers CSV qu'il
    y a de catégories
"""

        #Quatrième Etape#
"""
    Télécharger et enregistrer le fichier image de chaque livre
"""