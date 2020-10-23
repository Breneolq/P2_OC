class Book:

    def __init__(self, title, description, id, price_including_tax, price_excluing_tax, number_available, review_rating):
        
        self.title = title
        self.description = description
        self.id = id
        self.price_TTC = price_including_tax
        self.price_HT = price_excluing_tax
        self.number_available = number_available
        self.review_rating = review_rating
