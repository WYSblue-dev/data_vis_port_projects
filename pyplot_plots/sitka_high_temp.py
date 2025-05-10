from pathlib import Path

import csv

from datetime import datetime as dt

path = Path('/Users/wjerriii/Desktop/sitka_weather_2021_simple.csv')

# uses splitlines method of str class to create a list of all the data from the csv
lines = path.read_text(encoding='utf-8').splitlines()

# use the method reader to split catagories into rows(lists)
reader = csv.reader(lines)

# looks at the firs trow utilizing the next() function
header_row = next(reader)

# shows us our catagory labels for the colums of the csv
print(header_row)

# for loop wiht the enumerate function to shows both our index position and value
# notice this is specific to the first row. its shoing us the colum values.
for index, colum_row in enumerate(header_row):
    # simple print proof
    print(index, colum_row)

# empty list to adds the tmax values to
highs = []
dates = []

# we loop over the lists(rows) ew've obtained from reader and now knpw their 
# indexes to properly obtain the data.
for row in reader:
    high = int(row[4])
    highs.append(high)
    date = dt.strptime(row[2], '%Y-%m-%d')
    dates.append(date)