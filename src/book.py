class Book:

    def __init__(self, title, 
    universal_product_code, price_including_tax,
    price_excluding_tax, number_available, 
    product_description, category,
    review_rating, image_url):
        self.title = title
        self.universal_product_code = universal_product_code
        self.price_including_tax = price_including_tax
        self.price_excluding_tax =   price_excluding_tax
        self.number_available = number_available
        self.product_description = product_description
        self.category = category
        self.review_rating = review_rating
        self.image_url = image_url
    
