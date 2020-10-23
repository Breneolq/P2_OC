import csv

class Csv_writer:

    def __init__(self, file):
        self.file = file
    
    def write_in_csv(self):
        test_writer = csv.writer(self.file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        test_writer.writerow(['TEST'])
            