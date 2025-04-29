import matplotlib.pyplot as plt

months_data = list(range(1,11))
weeks_data = [month*4 for month in months_data] 
# we were given a ValueError here due to mismathch of 
# second values in the range in other words matplotlib needs 
# the same number of indexed elements to properly function. 
# So be sure to have the same number of elements. print calls with len would
# seem to porbably prove to be usful in this manner wioht a conditiona;l test.

plt.style.use('ggplot')

fig, ax = plt.subplots()

ax.plot(weeks_data, months_data, linewidth=2)

ax.set_title("Time Visual Representation".upper(), fontsize=16)

ax.set_xlabel("Weeks Remaining", fontsize=12)
ax.set_ylabel("Months Remaining", fontsize=12)

ax.tick_params(labelsize=18)

plt.show()