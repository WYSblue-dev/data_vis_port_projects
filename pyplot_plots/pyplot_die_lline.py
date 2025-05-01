import matplotlib.pyplot as plt

from die_class import Die

d_6 = Die()

results = [d_6.roll_die() for num in range(1, 10001)]

poss_num = range(1, d_6.num_sides+1)
frequencies = [results.count(num) for num in poss_num]

plt.style.use('ggplot')

fig , ax =plt.subplots(figsize=(15,9))

ax.bar(list(poss_num), frequencies, color='brown', edgecolor='black', linewidth=2)

ax.set_title("Showing frequnecies of d6".upper(), fontsize=22, c='grey')

ax.set_xlabel('value of side'.upper(), fontsize=16, c='blue')

ax.set_ylabel('frequency'.upper(), fontsize=16, c='blue')

plt.show()

