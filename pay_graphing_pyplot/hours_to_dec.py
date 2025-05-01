import matplotlib.pyplot as plt

# not needed since datetime calls this internally
# from time import time

from datetime import datetime as dt

# I know - time.time() produces epoch which .now() does this for us
date = dt.now()

# duh
weeks_in_year = 52

# need to know what this [1] in particutlar is doing here.
# after typing a comment later realize it's pulling value from tuple
current_week = date.isocalendar()[1]
# simple print call to show week
print(current_week)


# our weeks equals a list ranging from the current weeks gotten from
# isocalender()[1] which is a formatted tuple with (year, week num, week day)
# +1 is due to how the range function works.
weeks = list(range(current_week, weeks_in_year+1))

# simple print call to show weeks list
print(weeks)
print(len(weeks))

#current_weeks_left =  52 - (current number being looped over in weeks)
# the list comprehension here is nice because it lets us manage the process of
# doing the arithimitic easliy. this list wil also be as long as the 
current_weeks_left = [weeks_in_year - w for w in weeks]
# simple print call to show the list we've obtained
print(current_weeks_left)
print(len(current_weeks_left))

plt.style.use('ggplot')

fig, ax = plt.subplots()

ax.plot(weeks, current_weeks_left, linewidth=2, linestyle='-.')

ax.set_title("Time Visual Representation".upper(), fontsize=18)

ax.set_xlabel("Total Weeks In year", fontsize=16)
ax.set_ylabel("Weeks Left", fontsize=16)

# ax.invert_xaxis()

ax.set_aspect('equal')

ax.tick_params(labelsize=18)

plt.show()