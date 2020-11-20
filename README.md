Bonjour,

Petit point sur le programme.

Le programme va acceder à la première page du site. Il va chercher toutes les catégories et en faire une liste.
Il va ensuite parcourir cette liste et récupérer tous les livres.
Puis des livres, rechercher les informations suivantes afin de les renseigners dans un fichier csv:
    
    product_page_url
    universal_ product_code (upc)
    title
    price_including_tax
    price_excluding_tax
    number_available
    product_description
    category
    review_rating
    image_url

Afin de faire fonctionner ce programme, il vous faudra installer Python 3.9.0 grace au lien: https://www.python.org/downloads/

Une fois installé et à la racine du projet vous allez devoir créer un environnement virtuel.
Pour cela il va falloir installer le package necessaire:

'' pip install virtualenv ''

Creer un environnement virtuel:

'' virtualenv -p python3 env ''

Afin d'activer l'environnement virtuel:

'' source env/bin/activate ''

Suite à cela, pour installer tous les packages necessaires tapez la commande suivante:

'' pip install -r requirements.txt ''

Maintenant que vous avez tout ce qu'il vous faut, vous pouvez lancer le programme en faisant la commande:

'' python booktoscrape ''
