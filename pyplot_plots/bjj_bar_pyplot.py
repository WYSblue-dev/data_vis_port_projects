import matplotlib.pyplot as plt

from datetime import datetime as dt

# why dont we use parenthesis with this class call?
current_time = dt.now()

x = [
    'Arm Bar',
    'Heel Hook',
    'Triangle',  
    ]

y = [10, 20, 30]

# plt.style.use()

fig, ax = plt.subplots(figsize=(15,9))

ax.bar(x=x, height=y)

ax.set_title(current_time)
ax.set_xlabel("subs", fontsize=10)
ax.set_ylabel("frequnecy", fontsize=10)

plt.show()