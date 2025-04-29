import matplotlib.pyplot as plt

from pay_generator import GetPayData

pd = GetPayData(42, 500)

print(pd.y_val_hours)
plt.style.use("seaborn-v0_8-darkgrid")

fig, ax = plt.subplots()

ax.scatter(pd.x_point, pd.y_val_hours)

ax.axis([0, pd.total_hrs, 0, pd.max_dollar_shown])

ax.set_title("rate of wages scatter".title(), fontsize=24)
ax.set_xlabel("On the hour".upper(), fontsize=14)
ax.set_ylabel("Value at the hour".upper(), fontsize=14)

plt.tick_params(labelsize=10)

plt.show()