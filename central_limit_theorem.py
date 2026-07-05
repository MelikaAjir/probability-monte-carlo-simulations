import numpy as np
import matplotlib.pyplot as plt

# Number of experiments
n_experiments = 10000

# Number of random samples in each experiment
sample_size = 30

# Generate sample means
sample_means = []

for _ in range(n_experiments):
    sample = np.random.uniform(0, 1, sample_size)
    sample_means.append(np.mean(sample))

# Plot histogram
plt.hist(sample_means, bins=40, density=True, alpha=0.75)

plt.title("Central Limit Theorem Simulation")
plt.xlabel("Sample Mean")
plt.ylabel("Frequency")

plt.savefig("central_limit_theorem_plot.png")
plt.show()
