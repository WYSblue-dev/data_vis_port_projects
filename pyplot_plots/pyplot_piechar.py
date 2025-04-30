import matplotlib.pyplot as plt

# this needs to be revised and look over for understanding.

sizes = [15, 30, 45, 10]
labels = ['Frogs', 'Hogs', 'Dogs', 'Logs']
colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue']
explode = (0, 0.2, 0, 0)  # "explode" the 2nd slice
plt.style.use('ggplot')

fig, ax = plt.subplots()

plt.pie(sizes, labels=labels, colors=colors, explode=explode,
        autopct='%1.1f%%', shadow=False, startangle=140)
plt.title('Custom Pie Chart Example')
plt.show()
