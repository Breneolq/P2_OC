"""
import csv 

class Csv:

    def __init__(self):
        pass

    def WriteInCSV(self, title, category, product_description, universal_product_code, price_including_tax, price_excluding_tax, number_available, review_rating, image_url):
        with open(category +'.csv', mode='w', newline='') as csv_file:
            test_writer = csv.writer(csv_file, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            test_writer.writerow(['title', 'category', 'product_description', 'universal_product_code', 'price_including_tax', 'price_excluding_tax', 'number_available', 'review_rating', 'image_url'])
            test_writer.writerow([title, category, product_description, universal_product_code, price_including_tax, price_excluding_tax, number_available, review_rating, image_url])
"""