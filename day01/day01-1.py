import numpy as np

masses = np.genfromtxt('input-1.csv',dtype=int)
fuel_total = 0

for module in range(len(masses)):
  fuel_total += (masses[module] / 3) - 2

print(fuel_total)
