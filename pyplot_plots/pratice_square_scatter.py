import matplotlib.pyplot as plt

x_values = range(1,1000)
y_values = [x**2 for x in x_values]

input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]

plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()

ax.scatter(x_values, y_values, c=x_values, cmap=plt.cm.inferno, s=1)

ax.set_title("Small Sqaure Plot", fontsize=18)

ax.set_xlabel("Value", fontsize=14)

ax.set_ylabel("Square Value", fontsize=14)

ax.axis([1, 1_000, 1, 750_000])

ax.tick_params(labelsize=10, labelcolor='red')
ax.ticklabel_format(style='')


# plt.savefig("pathname")
plt.show()


