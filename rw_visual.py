import matplotlib.pyplot as plt
from random_walk import RandomWalk

while True:
    rw = RandomWalk(50000)
    rw.fill_walk()
    point_numbers = list(range(rw.num_points))
    # Назначение области просмотра
    plt.figure(dpi=128, figsize=(10, 6))
    plt.scatter(rw.x_values, rw.y_values, s=1, cmap='inferno', c=point_numbers, edgecolor='none')
    # Выделение первой и последней точек
    plt.scatter(0, 0, c='green', edgecolors='none', s=100)
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=100)
    # Удаление осей
    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)

    plt.show()

    keep_running = input("Make another walk? (y/n)")

    if keep_running == 'n':
        break
