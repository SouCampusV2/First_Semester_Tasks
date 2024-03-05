# import numpy as np
# import matplotlib.pyplot as plt
# # Программа запускается довольно долго, так что подождте около минуты
# def random_walk(N, num_trials):
#     # Список ждля средних значений
#     average_squares = []
    
#     for n in range(1, N + 1):
#         total_squares = 0
        
#         for _ in range(num_trials): # Выполняется 5000 раз вычисление оси
#             x = 0
#             for step in range(n):
#                 x += np.random.choice([-1, 1])  # Случайное перемещение вдоль оси Ox
#             total_squares += x**2
        
#         average_squares.append(total_squares / num_trials) # Добавляет средний квадрат смещения для текущего n
    
#     return average_squares

# N_values = list(range(10, 200, 10))  # Шаг от 1 до 200 потому что если сделать шаг 500 - то программа очень долго запускается и может выдать ошибку
# num_trials = 500

# average_squares = random_walk(N_values, num_trials)  # Используем 500 шагов для построения графика
    
# plt.plot(N_values, average_squares, label='Средний квадрат смещения')
# # plt.plot(N_values, np.array(N_values), linestyle='--', label='Прямая пропорциональности')

# plt.title('Случайные блуждания')
# plt.xlabel('Число шагов (N)')
# plt.ylabel('Средний квадрат смещения')
# plt.legend()

# plt.show()


import numpy as np
import matplotlib.pyplot as plt

def random_walk(N, num_trials):
    mean_square_displacement = np.zeros(N + 1)

    for _ in range(num_trials):
        positions = np.zeros(N + 1)

        for step in range(1, N + 1):
            # Случайное блуждание по оси Ox
            positions[step] = positions[step - 1] + np.random.normal()

        mean_square_displacement += positions**2

    mean_square_displacement /= num_trials

    return mean_square_displacement

def plot_random_walk():
    np.random.seed(42)  # Для воспроизводимости результатов

    max_N = 50
    num_trials = 500

    N = 10
    mean_square_displacement = random_walk(N, num_trials)

    # Построение графика
    steps = [step for step in range(N + 1)]
    plt.plot(steps, mean_square_displacement, label=f'N={N}')

    plt.xlabel('Число шагов (N)')
    plt.ylabel('Средний квадрат смещения (S^2)')
    plt.legend()
    plt.show()

# Вызываем функцию без явного условия if __name__ == "__main__":
plot_random_walk()
