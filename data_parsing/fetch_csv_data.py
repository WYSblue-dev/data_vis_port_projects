from pathlib import Path

# this import is here but we dont need to use it right now.
# learned here that csv is treated as text when read into memory as such.

import csv

class FetchCSV:
    """Used to fetch .csv file type data from a path obj."""

    def __init__(self, path_name):
        """Iinitilaizes the instance iteslf with the atts it needs and the arg expected"""
        self.path = Path(f'{path_name}.csv')
        
    def read_get_csv(self):
        """return the data obtained from the file we read in that's a csv."""
        content = self.path.read_text(encoding='utf-8')
        self.csv_data = content

    def show_csv_data(self):
        """Used to perfomr a print call to see what data was containted in pour .csv"""
        print(self.csv_data)


# COOL FIRST EXAMPLE OF US USING .CSV DATA.
# see_csv = FetchCSV('data_parsing/data_files/industry')

# see_csv.read_get_csv()

# see_csv.show_csv_data()

# local_csv_data = see_csv.csv_data

# for word in local_csv_data.split(' '):
#     print(word.lower())