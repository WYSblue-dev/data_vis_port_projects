import csv
from pathlib import Path
from datetime import datetime as dt

class CsvData():
    """This classes primary use is to make it easier to work with data parsing csv files. Reducing
    the amnount of repeated code we have to type for corresponding plots. Simply pass the class the
    csv file data then work with data as you need."""

    def __init__(self, pathname):
        """Initializes the class with the atts and setup it needs. Expecting
        to get a path name for the csv file you want to parse."""
        # assigning a path obj to work with in class
        # it will be worth looking at what to do if the file doesnt exist
        self.path = Path(pathname)
        self.lines = self._check_path_get_content()
        self.reader = csv.reader(self.lines)
        self.header_row = self._get_header_row()

        self.unique_id = None

    def _check_path_get_content(self):
        """Used to check the file path before we work with it. Returns True"""
        while True:
            try:
                lines = self.path.read_text(encoding='utf-8').splitlines()
            except FileNotFoundError:
                self.path = Path(input(f"The file path given doesn't exist or there's a typo.\npath: "))
                continue
            else:
                return lines
                break

    def _get_header_row(self):
        """Used to get the colum(cata) assignes to its corresponding index."""
        return next(self.reader)

    def show_header_row(self):
        """Shows us e the header row conviently."""
        for index, colum_name in enumerate(self.header_row):
            print(index, colum_name)

    def _check_unique_ids(self):
        """Used to check if the date persist. If it doesn't then we'll have to have the user
        inpu the catagory they prefer from the options in the terminal ehih would be the 
        header row."""
        for colum_name in self.header_row:
            if colum_name.index('date') == 'date':
                return True
                
            
    def index_csv_data(self, unique_id):
        """Used to index the csv data to be able work with it more effiecently instead of 
        looping over the reader every time. Dictionaries would seem to be beneficial.
        Expecting to find a unique ID for the purpose of making a useful index. To find the 
        ID we wnt though we need to use the get_show_header_row(). After looking at the results we
        can determine what we want our unique id to be. With that being said we could add a prompt
        in the terminal to select the index of unique ids we want to use. something like to show
        the header row make the decision and then format"""
        dates = []
        for row in self.reader:
            unique_id = dt.strptime(row[2], '%Y-%m-%d')
            dates.append(unique_id)