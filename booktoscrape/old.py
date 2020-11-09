"""
import csv


    def WriteInCSV(title, category, product_description, universal_product_code, price_including_tax, price_excluding_tax, number_available, review_rating, image_url):
        with open(category +'.csv', mode='w', newline='') as test_file:
            test_writer = csv.writer(test_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            test_writer.writerow(['title', 'category', 'product_description', 'universal_product_code', 'price_including_tax', 'price_excluding_tax', 'number_available', 'review_rating', 'image_url'])
            test_writer.writerow([title, category, product_description, universal_product_code, price_including_tax, price_excluding_tax, number_available, review_rating, image_url])

    WriteInCSV(title, category, product_description, universal_product_code, price_including_tax, price_excluding_tax, number_available, review_rating, image_url)
"""