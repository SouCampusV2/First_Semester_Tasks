import numpy as np
import matplotlib.pyplot as plt

# Исходные параметры
m1 = 0.05
m2 = 0.2
m = 0.1
R = 0.03
l = 0.1
dt = 0.02
Iner = m * R**2 / 2 + m1 * l**2

# Начальные условия
t = 0
i = 0
w = 0
fi = 0

# Создание списков для хранения данных
time_list = []
eps_list = []
w_list = []
fi_list = []

# Моделирование затухающих колебаний
while t < 50:
    t = t + dt
    i = i + 1
    eps = (m2 * 9.8 * R - m1 * 9.8 * l * np.sin(fi) - 0.02 * w) / (Iner + m2 * R**2)
    w = w + eps * dt
    fi = fi + w * dt
    
    # Добавление данных в списки
    time_list.append(t)
    eps_list.append(eps)
    w_list.append(w)
    fi_list.append(fi)

# Построение фазовой кривой
plt.figure(figsize=(8, 6))
plt.plot(fi_list, w_list)
plt.title('Phase Diagram')
plt.xlabel('Angle (fi)')
plt.ylabel('Angular Velocity (w)')
plt.show()
