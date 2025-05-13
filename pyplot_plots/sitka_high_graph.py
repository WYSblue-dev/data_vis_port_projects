import matplotlib.pyplot as plt

import sitka_temps as st

# we foigured out we can slice her but with the use of the fig.autofmt_xdates()
# it relieves us from slicing here.
sitka_dates = st.dates

sitka_highs = st.highs

sitka_lows = st.lows

plt.style.use('seaborn-v0_8')

fig, ax = plt.subplots(figsize=(15,9))

# notice we utilize 2 plots here with the same x values passed and the way
# that iinteracts with the autofmt_xdate seems important
# we just learned about alpha here as well which controls the colors trsansperency
# alpha work from 0-1 1 being completely gone.
ax.plot(sitka_dates, sitka_highs, linewidth=1.5, color='red', alpha=0.8, label='Sitka Highs')
ax.plot(sitka_dates, sitka_lows, linewidth=1.5, color='blue', alpha=0.8, label='Sitka Lows')
# facecolor is a new kwarg specific to the fill_between methos as far as I know
ax.fill_between(sitka_dates, sitka_highs,sitka_lows, alpha=.6, facecolor='orange', label='Sitka Temp Range')

ax.set_title('Sitka Alaska Daily High and Low Temps - 2021', color='brown', fontsize=24)

ax.set_xlabel("Dates(2021)", color='gray', fontsize=14)

ax.set_ylabel('Tempature (F)', color='gray', fontsize=14)

# changes the size of our tick_params on both axes
# grid_color is new to us I really like how it can make our plots pop out.
ax.tick_params(labelsize=18, grid_color='tan')

# changeas the color and size of our x axis
ax.tick_params(axis='x', labelsize=12, labelcolor='blue')

# changeas the color and size of our y axis
ax.tick_params(axis='y', labelsize=18, labelcolor=(1, .2, .1))

# we used this on our own to give our plots more information
# we though to call on a single plot but fig makes sense in the same way the 
# fig.autofmt_xdates makes sense.
fig.legend()

# we call this on the figure in the case of having multiple plots this would
# auto format them accordingly. We init thought why not ax for indi but this is 
# more convient for us to work with
fig.autofmt_xdate()

plt.savefig('sitka_high_low.png', bbox_inches='tight')

plt.show()