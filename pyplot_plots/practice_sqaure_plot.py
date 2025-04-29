import matplotlib.pyplot as plt

# emty list to store data
x_y_val = []

# data to be used could be imported with the way we seperate and manage the data
# would be beneifical to set up classes specific in this way more than likely
# empty dict to store data
square_data = {}
# generate numerical data with for loop from 1:16 kep in mind these will be key:value pairs not set
# if you want a set that's where the enumerate comes into play.
for number in range(1,17):
    square_data[number] = number
print(f"square_data - {square_data}")

# nmaybe this would be useful for scatters?
# this enumerate creates the sets needed for something like making a scatter plot.
for index, (placeholder, value) in enumerate(square_data.items()):
    x_y_val.append((placeholder, value))
print(f"x_y_val - {x_y_val}")

# empty list to store data
x_value = []
y_value = []

# maybe this will be usful for plotting.
for key, value in square_data.items():
    x_value.append(key)
    y_value.append(value)
print(f"x_value - {x_value}\ny_value - {y_value}")
# use with one of the styles avaible through matplotlib. Must take place before fig
plt.style.use('seaborn-v0_8')
# creates 2 obj instances. fig is figure of the graph, ax is the axes or the area to be used
# a distinct note here is to say that the axis is the x or y in particualr with the ticks etc...
# overall this create the template for the graph itself...boiler plate not lebals
fig, ax = plt.subplots()

# this plots our data points
# the kwarg linewidth changes the width of our plot line.
# note: look at other keyword args to find unique changes tot make yuor plots and graphs cool
ax.plot(x_value, y_value, linewidth=2, color='cyan')

ax.set_title("Squares".upper(), fontsize=18)
ax.set_xlabel("Square of Values", fontsize=14)
ax.set_ylabel("Value", fontsize=14)

# sets the size and color of our ticks
ax.tick_params(labelsize=10, labelcolor='red')

# sets the range essentially of the x and y axis. we start at 1 and this makoes our graph more
# visually appealing in that regaurd.
ax.axis([1, 16, 1, 16])

# path = Path('where/to/save/output')
# could use save fig to save in the working dir or to the specified file output path
# the kwarg passed cleans up the whitespace aroung the figure
# if don't pass a particular 'path' to save, saves at working dir with the save spec name
# plt.savefig("Path", bbox_inches='tight')

# trims the viewer up.
# plt.tight_layout()

# opens the matplotlib viewer with the figure and it's configed axes.
plt.show()