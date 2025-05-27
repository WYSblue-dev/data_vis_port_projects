import matplotlib.pyplot as plt

from pay_generator import GetPayData

# would be cool to make it to where we ask to repeat the scatter plot but leave 
# the previous plot shown so someone could see how maybe diffrent hours in a week
# compares.



# obtaining data from class we created from scratch
pd = GetPayData(42)
hour_data = pd.get_format_hrs_list()

rate_at_hour_data = pd.get_rate_to_hour_data(hour_data)

plt.style.use("seaborn-v0_8-darkgrid")

fig, ax = plt.subplots(figsize=(15,9))

ax.scatter(range(len(rate_at_hour_data)), rate_at_hour_data, c=rate_at_hour_data,
           cmap=plt.cm.inferno)

ax.axis([0, len(rate_at_hour_data), pd.rate, rate_at_hour_data[-1]])

ax.set_title(f"rate of wages {pd.rate}".upper(), fontsize=24, c='lime')
ax.set_xlabel("hour".title(), fontsize=14, c='red')
ax.set_ylabel("Value at hour".title(), fontsize=14, c='orange')

ax.tick_params(labelcolor='black', labelsize=14, width=1,
               size=3, color='purple', grid_color='black')

# line caused the tick makes to be spaced by the int passed as indi but way too
# many marks for readibility of the graph
# ax.set_xticks(list(range(len(pay_data))))
plt.show()