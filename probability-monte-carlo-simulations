import numpy as np
import matplotlib.pyplot as plt

n_points = 100000

x = np.random.uniform(-1, 1, n_points)
y = np.random.uniform(-1, 1, n_points)

inside_circle = x**2 + y**2 <= 1

pi_estimate = 4 * np.sum(inside_circle) / n_points

print(f"Estimated Pi: {pi_estimate}")

plt.figure(figsize=(6,6))
plt.scatter(
    x[inside_circle],
    y[inside_circle],
    s=1,
    alpha=0.5,
    label="Inside Circle"
)

plt.scatter(
    x[~inside_circle],
    y[~inside_circle],
    s=1,
    alpha=0.5,
    label="Outside Circle"
)

plt.title(f"Monte Carlo Estimation of Pi\nEstimate = {pi_estimate:.5f}")
plt.legend()
plt.show()
