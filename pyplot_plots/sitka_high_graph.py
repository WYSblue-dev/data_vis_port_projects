import matplotlib.pyplot as plt

import sitka_high_temp

x_value = sitka_high_temp.dates[0:40]

y_value = sitka_high_temp.highs[0:40]

plt.style.use('seaborn-v0_8')

fig, ax = plt.subplots(figsize=(15,9))

fig.autofmt_xdate()

ax.plot(x_value, y_value, linewidth=3, color='red')

ax.set_title('Sitka Alaska High Temps Jan', fontsize=24)

ax.set_xlabel("Dates", fontsize=14)

ax.set_ylabel('Tempature (F)', fontsize=14)

ax.tick_params(labelsize=8, color='orange')

plt.show()