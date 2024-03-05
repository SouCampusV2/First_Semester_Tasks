import matplotlib.pyplot as plt
import numpy as np

# Инициализация начальных значений
t = 0
x, y = 0, 0

# Создание списков для хранения координат
x_values, y_values = [x], [y]

# Цикл для обчисления движения Броуновской частицы
while t < 20:
    t += 0.05
    a = 2 * np.pi * np.random.rand()
    L = np.random.rand()
    x += L * np.cos(a)
    y += L * np.sin(a)

    x_values.append(x)
    y_values.append(y)

# Визуализация траектории Броуна
plt.plot(x_values, y_values, '-o')
plt.title('Броуновское движение')
plt.xlabel('X-координата')
plt.ylabel('Y-координата')
plt.show()



