import matplotlib.pyplot as plt

values = list(range(1,5001))
cubes = [x**3 for x in values]

plt.scatter(values, cubes, c=values, cmap='inferno')

plt.show()