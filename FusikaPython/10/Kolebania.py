import numpy as np
import matplotlib.pyplot as plt

def spring_pendulum_damped(mass, spring_constant, damping_coefficient, initial_displacement, initial_velocity, time_step, num_steps):
    # Инициализация массивов для хранения данных
    displacement = np.zeros(num_steps)
    velocity = np.zeros(num_steps)
    time = np.zeros(num_steps)

    # Установка начальных условий
    displacement[0] = initial_displacement
    velocity[0] = initial_velocity

    # Итерационное моделирование движения пружинного маятника
    for i in range(1, num_steps):
        time[i] = time[i-1] + time_step
        acceleration = (-spring_constant * displacement[i-1] - damping_coefficient * velocity[i-1]) / mass
        velocity[i] = velocity[i-1] + acceleration * time_step
        displacement[i] = displacement[i-1] + velocity[i] * time_step

    return time, displacement, velocity

# Параметры пружинного маятника
mass = 0.4  
spring_constant = 100.0  
damping_coefficient = 2  

# Начальные условия
initial_displacement = 0.3  
initial_velocity = 1

# Параметры моделирования
time_step = 0.01  
num_steps = 1000

# Моделирование
time, displacement, velocity = spring_pendulum_damped(mass, spring_constant, damping_coefficient, initial_displacement, initial_velocity, time_step, num_steps)

# Построение фазовой кривой
plt.plot(displacement, velocity)
plt.title('Фазовая кривая пружинного маятника с затуханием')
plt.xlabel('x')
plt.ylabel('v(x)')
plt.grid()
plt.show()
