from csv_writer import Csv_writer

class File:


    def __init__(self, category):
        self.category = category
        
    
    def open_file(self):
        with open(self.category + 'csv', mode='w', newline='') as openfile:
            write_test = Csv_writer(openfile)
            write_test.write_in_csv()