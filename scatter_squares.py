import matplotlib.pyplot as plt

# plt.scatter(2, 4, s=200)

x_values = list(range(1, 1001))
y_values = [x**2 for x in x_values]

plt.scatter(x_values, y_values, s=40, edgecolor='none', c=y_values, cmap=plt.cm.Blues)

# Назначение диапазона для каждой оси
plt.axis([0, 1100, 0, 1100000])
plt.savefig('squares_plot.png', bbox_inches='tight')