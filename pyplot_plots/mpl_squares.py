import matplotlib.pyplot as plt

input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]

# I used this dataset for fun
# squares = [value**2 for value in range(100)]

# THIS HAS TO BE CALLED BOEFORE SUBPLOTS TO TAKE EFFECT!!
# sets the styled we checked to see if we had.
# in the terminal with a acitvaited env.
# import matplotlib.pyplot as plt
# plt.style.available
# this give use a list of installed styles that we have access to.
plt.style.use('seaborn-v0_8-darkgrid')

# fig is the refrence t the entire figure itself
# ax is in refrence to the individual points(plot) that get plotted
# plt.subplots() is standard to create the template figure(display surface) and setting up ax(plot)
fig, ax = plt.subplots()
# .plot() is used to try to plot the data in a meaningful way.
# without this method the figure wouldn't have any data to plot.
# it would be emtpy.
ax.plot(input_values, squares, linewidth=3)

# set the chart title and x,y labels
ax.set_title("Squares", fontsize=24) # name of graph
ax.set_xlabel("Value", fontsize=14) # values with sizing
ax.set_ylabel("Square of Value", fontsize=14) # Square of value with sizing

# sets the size of tick labels.
# what is the tick?
# that is in refernce tpo the numbers...those are ticks
ax.tick_params(labelsize=14)

# opens the matplotlib viewer and displaysthe plot.
plt.show()