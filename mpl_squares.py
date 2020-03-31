import matplotlib.pyplot as plt

input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]
plt.plot(input_values, squares, linewidth=5)

# Назначение заголовка диаграммы и меток осей
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of values", fontsize=14)
# Назначение шрифта делений на осях
plt.tick_params(axis='both', which='major', labelsize=14)

plt.show()