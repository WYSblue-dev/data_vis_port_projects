from datetime import datetime as dt
from pathlib import Path
import csv

import plotly.express as px
import pandas as pd # need to review this to work wiht dataframes when ready.
# the part we need to undrstand the most is how csv tab date fits into and works 
# with pandas dataframe


# san diego csv data
path = Path('data_files/csv_data/weather_related/san_diego_ca.csv')
lines = path.read_text(encoding='utf-8').splitlines()
reader = csv.reader(lines)
header_row = next(reader)

# index is crucial for flex
date_index = header_row.index('DATE')
temp_high_index = header_row.index('TMAX')
temp_low_index = header_row.index('TMIN')

dates_s, temp_highs_s, temp_lows_s = [], [], []

for row in reader:
    current_date = dt.strptime(row[date_index], "%Y-%m-%d")
    try:
        temp_high = int(row[temp_high_index])
        temp_low = int(row[temp_low_index])
    except ValueError:
        print(f'Item value doesnt exist for {current_date}')
    else:
        dates_s.append(current_date)
        temp_highs_s.append(temp_high)
        temp_lows_s.append(temp_low)

path = Path('data_files/csv_data/weather_related/zanesville_oh.csv')
lines = path.read_text(encoding='utf-8').splitlines()
reader = csv.reader(lines)

header_row = next(reader)

date_index = header_row.index('DATE')
high_temp_index = header_row.index('TMAX')
low_temp_index = header_row.index("TMIN")


# zaneville csv data
dates_z, high_temps_z, low_temps_z = [], [], []

for row in reader:
    date = dt.strptime(row[date_index], "%Y-%m-%d")
    try:
        high_temp = int(row[high_temp_index])
        low_temp = int(row[low_temp_index])
    except ValueError:
        print(f'Item value doesnt exist for {date}')
    else:
        dates_z.append(date)
        high_temps_z.append(high_temp)
        low_temps_z.append(low_temp)


# starting the plotly plot
title = "Tempature(F) at Zanesville, OH and San Diego, CA"
labels = {'x':'Dates', 'value':'Tempatures(F)'}

fig = px.line(x=dates_z, y=[high_temps_z, temp_highs_s,], labels=labels, title=title)

fig.update_layout(
    legend=dict(
        title=dict(text="Trend"))
        )

fig.show()