import csv
import requests
from bs4 import BeautifulSoup
import urllib.parse

url_home = 'http://books.toscrape.com/'
url_produit = 'http://books.toscrape.com/catalogue/in-a-dark-dark-wood_963/index.html'
response = requests.get(url_produit)
response.encoding = 'utf-8'


if response.ok:
    soupe = BeautifulSoup(response.text, features="html.parser")
    product_page_url = url_produit
    
def SearchInBoard(id, soup):
    for i in soup.find_all("th"):
        if i.text.strip() == id:
            return(i.find_next("td").text.strip())

def SearchDescription(soup):
    meta = soup.find('meta', {'name': 'description'})
    description = meta['content']
    return(description)

def SearchTitle(soup):
    return(soup.find('div', {'class': 'col-sm-6 product_main'}).find('h1').text.strip())

def SearchCategory(soup):
    category = soup.find('ul', {'class': 'breadcrumb'}).find_all(['a'])
    return(category[2].text.strip())

def SearchImageUrl(soup, url):
    img = soup.find('div', {'class': 'thumbnail'}).find('div', {'class': 'carousel-inner'}).find('div', {'class': 'item active'}).find('img')
    link = img['src']
    return urllib.parse.urljoin(url, link)

def WriteInCSV(title, category, product_description, universal_product_code, price_including_tax, price_excluding_tax, number_available, review_rating, image_url):
    with open(category +'.csv', mode='w', newline='') as test_file:
        test_writer = csv.writer(test_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        test_writer.writerow(['title', 'category', 'product_description', 'universal_product_code', 'price_including_tax', 'price_excluding_tax', 'number_available', 'review_rating', 'image_url'])
        test_writer.writerow([title, category, product_description, universal_product_code, price_including_tax, price_excluding_tax, number_available, review_rating, image_url])

universal_product_code = SearchInBoard("UPC", soupe)
price_including_tax = SearchInBoard("Price (incl. tax)", soupe)
price_excluding_tax = SearchInBoard("Price (excl. tax)", soupe)
number_available = SearchInBoard("Availability", soupe)
review_rating = SearchInBoard("Number of reviews", soupe)
product_description = SearchDescription(soupe)
title = SearchTitle(soupe)
category = SearchCategory(soupe)

image_url = SearchImageUrl(soupe, url_home)

WriteInCSV(title, category, product_description, universal_product_code, price_including_tax, price_excluding_tax, number_available, review_rating, image_url)

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