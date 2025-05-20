from pathlib import Path
import csv
from datetime import datetime as dt

import matplotlib.pyplot as plt

# znaesville weather data
path_z = Path('/Users/wjerriii/Desktop/zanesville_oh.csv')
lines = path_z.read_text(encoding='utf-8').splitlines()
reader = csv.reader(lines)
header_row = next(reader)

# set up indexing
date_index = header_row.index('DATE')
temp_high_index = header_row.index('TMAX')
temp_low_index = header_row.index('TMIN')

dates, temp_highs, temp_lows = [], [], []

for row in reader:
    date = dt.strptime(row[date_index], '%Y-%m-%d')
    try:
        temp_high = int(row[temp_high_index])
        temp_low = int(row[temp_low_index])
    except ValueError:
        print(f'Missing date for{date}')
    else:
        dates.append(date)
        temp_highs.append(temp_high)
        temp_lows.append(temp_low)

# san diego weather data
path_s = Path('/Users/wjerriii/Desktop/san_diego_ca.csv')
lines = path_s.read_text(encoding='utf-8').splitlines()
reader = csv.reader(lines)
header_row = next(reader)

dates_2, temp_highs_2, temp_lows_2 = [], [], []

# set up indexing
date_index_2 = header_row.index('DATE')
temp_high_index_2 = header_row.index('TMAX')
temp_low_index_2 = header_row.index('TMIN')

for row in reader:
    date = dt.strptime(row[date_index_2], '%Y-%m-%d')
    try:
        temp_high = int(row[temp_high_index_2])
        temp_low = int(row[temp_low_index_2])
    except ValueError:
        print(f'Missing date for{date}')
    else:
        dates_2.append(date)
        temp_highs_2.append(temp_high)
        temp_lows_2.append(temp_low)

plt.style.use('seaborn-v0_8')

fig, ax = plt.subplots(figsize=(15,8))

ax.plot(dates, temp_highs, label='Temp Highs', color='blue', linewidth=1.5, alpha=.6)
ax.plot(dates_2, temp_highs_2, label='Temp Highs', color='red', linewidth=1.5, alpha=.6)
ax.fill_between(dates_2, temp_highs_2, temp_highs, facecolor='black', alpha=1, label="Temp. Range")

ax.set_title("Ohio and Cali Tempatures(F)", fontsize=24)
ax.set_xlabel('Dates', fontsize=14)
ax.set_ylabel("Tempature(F)", fontsize=14)

ax.tick_params(axis='x', labelcolor='brown', labelsize=16)
ax.tick_params(axis='y', labelcolor='limegreen', labelsize=20)
ax.tick_params(grid_color='tan', grid_alpha=.5)

fig.legend()

fig.autofmt_xdate()

plt.show()