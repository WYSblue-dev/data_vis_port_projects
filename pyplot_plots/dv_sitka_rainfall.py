from pathlib import Path

import csv

from datetime import datetime as dt

import matplotlib.pyplot as plt

# death valley data parsing
path_dv = Path('/Users/wjerriii/Desktop/death_valley_2021_full.csv')

lines = path_dv.read_text(encoding='utf-8').splitlines()

reader = csv.reader(lines)

header_row = next(reader)

for index, colum_name in enumerate(header_row):
    print(f"DV - {index}, {colum_name}")
print()

dates_dv = []
rain_days_dv = []

for row in reader:
    try:
        rained = float(row[3])
    except ValueError:
        continue
    else:
        date = dt.strptime(row[2], '%Y-%m-%d')
        dates_dv.append(date)
        rain_days_dv.append(rained)


# sitka data parsing.
path_sit = Path('/Users/wjerriii/Desktop/sitka_weather_2021_full.csv')

lines = path_sit.read_text(encoding='utf-8').splitlines()

reader = csv.reader(lines)

header_row = next(reader)

for index, colum_name in enumerate(header_row):
    print(f"Sit - {index}, {colum_name}")

dates_sit = []
rain_days_sit = []

for row in reader:
    try:
        rained = float(row[5])
    except ValueError:
        continue
    else:
        date = dt.strptime(row[2], '%Y-%m-%d')
        dates_sit.append(date)
        rain_days_sit.append(rained)

plt.style.use("seaborn-v0_8")

fig, ax = plt.subplots(figsize=(15,8))

ax.plot(dates_dv, rain_days_dv, color='red', linewidth=1.5, alpha=1, label='Death Val')
ax.plot(dates_sit, rain_days_sit, color='limegreen', linewidth=1.5, alpha=1, label='Sitka')

ax.set_title("Rain in Sit and Death Val", fontsize=24)

ax.set_xlabel("Date Occured", fontsize=14, color='tan')

ax.set_ylabel("Amount occured", fontsize=14, color='tan')

ax.tick_params(labelsize=12, grid_color='black', grid_alpha=.3)
ax.tick_params(axis='x', labelcolor='grey')
ax.tick_params(axis='y', labelcolor='grey')

fig.autofmt_xdate()

fig.legend()

plt.show()