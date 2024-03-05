import random

def integrate_monte_carlo(func, a, b, n):
    
    # Вычисляет определенный интеграл функции методом Монте-Карло.

    # param func: Интегрируемая функция
    # param a: Нижняя граница отрезка интегрирования
    # param b: Верхняя граница отрезка интегрирования
    # param n: Количество случайных точек для метода Монте-Карло
    # return: Приближенное значение определенного интеграла
    
    count_inside = 0

    for _ in range(n):
        x = random.uniform(a, b)
        y = random.uniform(0, max(func(a), func(b)))

        if 0 <= y <= func(x):
            count_inside += 1

    area_rectangle = (b - a) * max(func(a), func(b))
    ratio_inside = count_inside / n

    return area_rectangle * ratio_inside

# Пример использования:
import math

def example_function(x):
    return math.sin(x)

a = 0
b = math.pi
n = 10000

result = integrate_monte_carlo(example_function, a, b, n)
print("Приближенное значение определенного интеграла:", result)
