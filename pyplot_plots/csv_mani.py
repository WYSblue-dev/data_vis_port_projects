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

        self.unique_id = None

    def _check_path_get_content(self):
        """Used to check the file path before we work with it. Returns True"""
        while True:
            try:
                lines = self.path.read_text(encoding='utf-8').splitlines()
            except FileNotFoundError:
                print(f"The file path given doesn't exist or there's a typo.\n{input('path: ')}")
                continue
            else:
                return lines
                break

    def get_show_header_row(self):
        """Used to get the colum(cata) assignes to its corresponding index."""
        self.header_row = next(self.reader)
        for index, colum_name in enumerate(self.header_row):
            print(index, colum_name)

    def index_csv_data(self, unique_id):
        """Used to index the csv data to be able work with it more effiecently instead of 
        looping over the reader every time. Dictionaries would seem to be beneficial.
        Expecting to find a unique ID for the purpose of making a useful index. To find the 
        ID we wnt though we need to use the get_show_header_row(). After looking at the results we
        can determine what we want our unique id to be. With that being said we could add a prompt
        in the terminal to select the index of unique ids we want to use. something like to show
        the header row make the decision and then format the data."""
        