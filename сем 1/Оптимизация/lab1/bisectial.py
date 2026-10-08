from matplotlib import pyplot as plt
import numpy as np
save_data = []
E = 1e-10
def find_interval(func, start=0, step=1e-2):
    interval = [start, start + step]
    while np.sign(func(interval[0])) == np.sign(func(interval[1])):
        interval[0] = interval[1]
        interval[1] += step
    return tuple(interval)

def find_solutions(func, interval):
    print("Итерация \t Значение \t Погрешность")
    iteration = 0
    c = None
    solutions = []
    while abs(interval[0] - interval[1]) > E:
        c = sum(interval) / 2
        fc = func(c)
        fa = func(interval[0])
        if np.sign(fc) == np.sign(fa):
            interval = [c, interval[1]]
        else:
            interval = [interval[0], c]
        solutions.append(c)
        print(f"{iteration} \t {sum(interval) / 2} \t {abs(interval[0] - interval[1])}")
        iteration += 1
    save_data.append((iteration, solutions))

    return sum(interval) / 2
def show_plot():
    plt.figure(figsize=(10, 10))
    for i, (iterations, solutions) in enumerate(save_data):
        a = plt.subplot(2, 4, i + 1)

        plt.plot(range(1, iterations + 1), solutions, marker="o", markersize=7)
        plt.title(f"Решение {i}")
        plt.xlabel("Итерации")
        plt.ylabel("Решение")
    plt.subplots_adjust(
        hspace=0.4
    )
    plt.show()