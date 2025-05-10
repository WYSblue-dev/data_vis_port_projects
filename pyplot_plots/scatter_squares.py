from pathlib import Path

import matplotlib.pyplot as plt

# x_values = [1, 2, 3, 4, 5]
# y_values = [1, 4, 9, 16, 25]

x_values = range(1,1001)
y_values = [x**2 for x in x_values]

alt_x = range(1,1001)
alt_y = [x**3 for x in x_values]

alt_x_2 = range(1,1001)
alt_y_2 = [x**2.5 for x in alt_x_2]

plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()

# this is a traditional graph s=10 specifies the scatter plot point size.
# color='purple' is used to changethe color of the point that is being plotted
ax.scatter(x_values, y_values, color='purple', s=10)

# self testing multiple scatters other line is cubed with the range set the same
# looking into color= scatter expects 0:1 not 0:255 so we divid our ints to be such
# division by 255 produces us with a decimal within that 0:1
# we could aslo pass these color values as (1, 1, .2)
ax.scatter(alt_x, alt_y, color=(250/255, 200/255, 20/255), s=8)

# 3rd scatter plot for testing but this time we'll use a color gradient
# find all your avaible color gradients at
# https://matplotlib.org/stable/users/explain/colors/
# colormaps.html#sphx-glr-users-explain-colors-colormaps-py
ax.scatter(alt_x_2, alt_y_2, c=x_values, cmap=plt.cm.inferno, s=5)


ax.set_title('Square Numbers', fontsize=20)
ax.set_xlabel('Value', fontsize=14)
ax.set_ylabel('Squared Values', fontsize=14)

plt.tick_params(labelsize=12)

# set the rsange for each axis
ax.axis([0, 1100, 0, 10_000_000])
# changes the notation of the ticks trad is 'sci'
ax.ticklabel_format(style='plain')

# let's import patlib to write it anywhere on our file system like a all_plots dir
# output_file = Path("all_plots/scatter_squares.png")

# this saves our plot as a .png to the same working directory the script is in.
# plt.savefig(output_file, bbox_inches='tight')

# this is a new merthod that we discovered through perplexity it makes it to where our
# information we display with our labels is visible when showinf through the viewer
plt.tight_layout()

# open up figure with the MatPlotLib gui(viewer).
# could auto saves somehow maybe, maybe even with a Path obj.
plt.show()