import matplotlib.pyplot as plt

from die_class import Die

d_6 = Die()

results = [d_6.roll_die() for num in range(1,10001)]

poss_num = range(1, d_6.num_sides+1)

frequencies = [results.count(result) for result in poss_num]

plt.style.use('grayscale')

fig, ax = plt.subplots(figsize=(15,9))

ax.scatter(poss_num, frequencies)

ax.set_title("Scattered die".title(), fontsize=24)

ax.set_xlabel('Possible values'.upper(), fontsize=14)

ax.set_ylabel('frequencies'.upper(), fontsize=14)

# ax.axis([0, 7, 0, 10001])
# it's crazy to see how when we look at the points plotted that if we dont set the axis to a higher
# how drastcally diffremn the graph is.
# also ha ing thoughts about maybe changing the point color onceit exceeds a certain value
# this would [oprbably be [retty easy to implament.

ax.tick_params()

plt.tight_layout()

plt.show()