import numpy as np
import matplotlib.pyplot as plt

n_flips = 10000

flips = np.random.choice([0, 1], size=n_flips)

running_mean = np.cumsum(flips) / np.arange(1, n_flips + 1)

plt.plot(running_mean)
plt.axhline(0.5, color='red')
plt.title("Law of Large Numbers")
plt.xlabel("Number of Flips")
plt.ylabel("Proportion of Heads")
plt.show()
