def integrate_trapezoidal_rule(func, a, b, n):
    
    # Вычисляет определенный интеграл функции методом трапеций.

    # param func: Интегрируемая функция
    # param a: Нижняя граница отрезка интегрирования
    # param b: Верхняя граница отрезка интегрирования
    # param n: Количество кусочков (разбиений)
    # return: Приближенное значение определенного интеграла
    
    h = (b - a) / n
    integral_sum = 0.5 * (func(a) + func(b))

    for i in range(1, n):
        integral_sum += func(a + i * h)

    return integral_sum * h

# Пример использования:
def example_function(x):
    return x**2

a = 0
b = 1
n = 1000

result = integrate_trapezoidal_rule(example_function, a, b, n)
print("Приближенное значение определенного интеграла:", result)
