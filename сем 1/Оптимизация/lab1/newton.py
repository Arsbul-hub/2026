from matplotlib import pyplot as plt
import numpy as np
save_data = []
E = 1e-10
def find_interval(func, start=0, step=1e-1):
    interval = [start, start + step]
    while np.sign(func(interval[0])) == np.sign(func(interval[1])):
        interval[1] += step
    return tuple(interval)

def find_solutions(func, derivative, interval):
    print("Итерация \t Значение \t Погрешность")
    iteration = 0
    solutions = []
    kx = sum(interval) / 2
    while True:
        kx_found = kx - func(kx) / derivative(kx)
        print(f"{iteration} \t {kx_found} \t {abs(kx_found - kx)}")
        iteration += 1
        solutions.append(kx_found)
        if abs(kx_found - kx) < E:
            break
        kx = kx_found


    save_data.append((iteration, solutions))
    return kx_found


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