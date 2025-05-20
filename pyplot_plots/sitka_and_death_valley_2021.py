from pathlib import Path
import csv
from datetime import datetime as dt

import matplotlib.pyplot as plt

import sitka_temps as st

# we foigured out we can slice her but with the use of the fig.autofmt_xdates()
# it relieves us from slicing here.
sitka_dates = st.dates

sitka_highs = st.highs

sitka_lows = st.lows

path = Path('/Users/wjerriii/Desktop/death_valley_2021_full.csv')

lines = path.read_text(encoding='utf-8').splitlines()

reader = csv.reader(lines)

header_row = next(reader)

for index, colum_name in enumerate(header_row):
    print(index, colum_name)

highs_dv = []
lows_dv = []
dates_dv = []

for row in reader:
    try:
        high = int(row[6])
        low = int(row[7])
        date = dt.strptime(row[2], '%Y-%m-%d')
    except ValueError:
        print(f"Missing data for {date} values(h,l) - {high} {low}")
    else:
        highs_dv.append(high)
        lows_dv.append(low)
        dates_dv.append(date)

plt.style.use('seaborn-v0_8')

fig, ax = plt.subplots(figsize=(15,8))

# death valley temps
ax.plot(dates_dv, highs_dv, linewidth=1.5, color='green', alpha=.6, label='High Temps.')
ax.plot(dates_dv, lows_dv, linewidth=1.5, color='blue', alpha=.6, label='Low Temps.')
ax.fill_between(dates_dv, highs_dv, lows_dv, facecolor='black', alpha=.3)

# sitka temps
# notice we utilize 2 plots here with the same x values passed and the way
# that iinteracts with the autofmt_xdate seems important
# we just learned about alpha here as well which controls the colors trsansperency
# alpha work from 0-1 1 being completely viewable.
ax.plot(sitka_dates, sitka_highs, linewidth=1.5, color='black', alpha=0.8, label='Sitka Highs')
ax.plot(sitka_dates, sitka_lows, linewidth=1.5, color='blue', alpha=0.8, label='Sitka Lows')
# facecolor is a new kwarg specific to the fill_between methos as far as I know
ax.fill_between(sitka_dates, sitka_highs, sitka_lows, alpha=.6, facecolor='orange', label='Sitka Temp Range')

# used to see areas of cross over of average temps
ax.fill_between(dates_dv, lows_dv, sitka_highs, facecolor='red', label='Diffrence of Temps')

ax.set_title('Death Valley and Sitka Highs and Lows 2021', fontsize=24)

ax.set_xlabel('Dates', fontsize=14, color='tan')

ax.set_ylabel('Tempatures', fontsize=16, color='tan')

fig.autofmt_xdate()

fig.legend()

plt.show()