import numpy as np
import matplotlib.pyplot as plt

# Dummy data
x = np.linspace(0, 10, 200)
y1 = np.sin(x)
y2 = 0.5 * np.cos(x) + 0.2

plt.figure(figsize=(10, 6))

# Plot the two curves
plt.plot(x, y1, label='y1 = sin(x)', color='blue')
plt.plot(x, y2, label='y2 = 0.5*cos(x) + 0.2', color='orange')

# Fill where y1 > y2
# assuming that we're passing the same data twice but with a diff where check
plt.fill_between(x, y1, y2, where=(y1 > y2), interpolate=True, color='green', alpha=0.4, label='y1 > y2')

# Fill where y1 <= y2
plt.fill_between(x, y1, y2, where=(y1 <= y2), interpolate=True, color='red', alpha=0.4, label='y1 <= y2')

plt.legend()
plt.xlabel('x')
plt.ylabel('y')
plt.title('Highlighting Crossover Areas Between Two Curves')
plt.grid(True)
plt.show()
