import numpy as np

masses = np.genfromtxt('input-1.csv',dtype=int)
fuel_total = 0

for module in range(len(masses)):
  fuel4module = (masses[module] / 3) -2
  fuel_total += fuel4module
  addtl_fuel = fuel4module
  while addtl_fuel > 0:
    addtl_fuel = (addtl_fuel / 3) - 2
    if addtl_fuel > 0:
      fuel_total += addtl_fuel

print(fuel_total)
