from pathlib import Path
import csv
from datetime import datetime as dt

import matplotlib.pyplot as plt

path = Path('/Users/wjerriii/Desktop/death_valley_2021_full.csv')

lines = path.read_text(encoding='utf-8').splitlines()

reader = csv.reader(lines)

header_row = next(reader)

for index, colum_name in enumerate(header_row):
    print(index, colum_name)

highs = []
lows = []
dates = []

for row in reader:
    try:
        high = int(row[6])
        low = int(row[7])
        date = dt.strptime(row[2], '%Y-%m-%d')
    except ValueError:
        print(f"Missing data for {date} values(h,l) - {high} {low}")
        print(header_row)
        print(row)
    else:
        highs.append(high)
        lows.append(low)
        dates.append(date)

plt.style.use('seaborn-v0_8')

fig, ax = plt.subplots(figsize=(15,9))

ax.plot(dates, highs, linewidth=1.5, color='red', alpha=.6, label='High Temps.')
ax.plot(dates, lows, linewidth=1.5, color='blue', alpha=.6, label='Low Temps.')
ax.fill_between(dates, highs, lows, facecolor='black', alpha=.3, label='Temp. Range')

ax.set_title('Death Valley Highs and Lows 2021', fontsize=24)

ax.set_xlabel('Dates', fontsize=14, color='tan')

ax.set_ylabel('Tempatures', fontsize=16, color='tan')

fig.autofmt_xdate()

fig.legend()

# plt.savefig('death_valley_high_low.png', bbox_inches='tight')

plt.show()