import plotly.express as px

from die import Die

die_1 = Die()
die_2 = Die()
die_3 = Die()

results = []
for roll in range(1,6_000_001):
    roll = die_1.roll_die() * die_2.roll_die() * die_3.roll_die()
    results.append(roll)

# be mindful of what we're trying to accomplish. If we roll 2 die it's not poss
# to get a value of 1.
possible_rolls = range(3, (die_1.num_sides + die_2.num_sides + die_3.num_sides)+1)
frequencies = []
for frequnecy in possible_rolls:
    frequnecy = results.count(frequnecy)
    frequencies.append(frequnecy)

title = 'rolling 3 d6 die'.title()
labels = {'x':'Possible Value', 'y':'Frequency'}
fig = px.bar(x=possible_rolls, y=frequencies, title=title, labels=labels, opacity=.5)

fig.update_layout(xaxis_dtick=1)

fig.show()