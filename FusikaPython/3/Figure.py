import numpy as np
import matplotlib.pyplot as plt

def lissajous_curve(A1, A2, n, t):# Pассчета координат точек фигуры Лиссажу.
    x = A1 * np.cos(t)
    y = A2 * np.sin(n * t)
    return x, y

def plot_lissajous(A1, A2, n):
    t = np.linspace(0, 2 * np.pi, 1000) # Cоздает массив t из 1000 точек в диапазоне от 0 до 2π. Это используется для задания угла в функции
    # Узнаем лучшую точку.
    x, y = lissajous_curve(A1, A2, n, t) # Pассчета координат точек фигуры Лиссажу.

    plt.figure(figsize=(8, 8)) # Создает новый график с размерами 8x8
    plt.plot(x, y, label=f'Фигура Лиссажу: A1={A1}, A2={A2}, n={n}') #Строит график фигуры Лиссажу
    plt.title('Фигура Лиссажу') #Задает заголовок графика.
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.grid(True)
    plt.show() # Показывает график.


A1 = 1.2 # Амлитуды колебаний
A2 = 2
n = 3/2  # Рациональная дробь
plot_lissajous(A1, A2, n)