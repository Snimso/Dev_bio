import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm.

# Seed for reproducibility
np.random.seed(42)

# Defining variables the temperature and diet conditions
temperatures = ['Low', 'Optimal', 'High']
diets = ['Standard', 'Nutrient-rich']

# Generating synthetic data for embryo viability
# We assume normal distributions centered at different means for each temperature
embryo_viability = {
    'Low': np.random.normal(40, 10, 100),  # Lower mean for adverse condition
    'Optimal': np.random.normal(70, 10, 100),  # Higher mean for optimal condition
    'High': np.random.normal(50, 10, 100)  # Intermediate mean for another adverse condition
}

# Generating synthetic data for maternal stress resilience
# Different means for different diets
maternal_resilience = {
    'Standard': np.random.normal(65, 10, 100),  # Lower resilience on standard diet
    'Nutrient-rich': np.random.normal(85, 10, 100)  # Higher resilience on nutrient-rich diet
}

# Plotting the results
fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(14, 6))
colors = ['red', 'green', 'blue']

# Plot for embryo viability across temperatures
for i, temp in enumerate(temperatures):
    data = embryo_viability[temp]
    count, bins, ignored = axes[0].hist(data, bins=15, alpha=0.7, label=f'{temp} Temp', density=True)

    # line of best fit through normal distribution
    mu, std = norm.fit(data)
    p = norm.pdf(bins, mu, std)
    axes[0].plot(bins, p, color=colors[i], linewidth=2)

axes[0].set_title('Embryo Viability Across Temperatures')
axes[0].set_xlabel('Viability (%)')
axes[0].set_ylabel('Density')
axes[0].legend()

# Plot for maternal stress resilience across diets
for i, diet in enumerate(diets):
    data = maternal_resilience[diet]
    count, bins, ignored = axes[1].hist(data, bins=15, alpha=0.7, label=f'{diet} Diet', density=True)

    # line of best fit through normal distribution
    mu, std = norm.fit(data)
    p = norm.pdf(bins, mu, std)
    axes[1].plot(bins, p, color=colors[i], linewidth=2)


axes[1].set_title('Maternal Stress Resilience Across Diets')
axes[1].set_xlabel('Resilience (%)')
axes[1].set_ylabel('Density')
axes[1].legend()


plt.tight_layout()
plt.show()