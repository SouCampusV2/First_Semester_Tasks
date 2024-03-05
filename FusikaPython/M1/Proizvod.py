def calculate_derivative(x_range, step_size, function_values):
    derivative_values = []

    for i in range(len(x_range)):
        x0 = x_range[i]
        h = step_size

        if i == 0:  # начальная точка
            derivative = (-function_values[i + 2] + 4 * function_values[i + 1] - 3 * function_values[i]) / (2 * h)
        elif i == len(x_range) - 1:  # конечная точка
            derivative = (function_values[i - 2] - 4 * function_values[i - 1] + 3 * function_values[i]) / (2 * h)
        else:  # внутренняя точка
            derivative = (function_values[i + 1] - function_values[i - 1]) / (2 * h)

        derivative_values.append(derivative)

    return derivative_values

# Пример использования:
import matplotlib.pyplot as plt

# Задаем функцию для тестирования (например, квадратичная функция)
def test_function(x):
    return x**2

# Задаем диапазон и шаг
x_range = [i for i in range(-10, 11)]
step_size = 1

# Вычисляем значения функции для каждой точки x
function_values = [test_function(x) for x in x_range]

# Вычисляем значения производной
derivative_values = calculate_derivative(x_range, step_size, function_values)

# Выводим результаты
print("Значения функции:", function_values)
print("Значения производной:", derivative_values)

# Рисуем графики
plt.plot(x_range, function_values, label='Функция')
plt.plot(x_range, derivative_values, label='Производная')
plt.legend()
plt.show()
