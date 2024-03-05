def integrate_simpsons_rule(func, a, b, n):
    
    # Вычисляет определенный интеграл функции методом парабол (Симпсона).

    # param func: Интегрируемая функция
    # param a: Нижняя граница отрезка интегрирования
    # param b: Верхняя граница отрезка интегрирования
    # param n: Количество кусочков (разбиений), должно быть четным
    # return: Приближенное значение определенного интеграла
    
    if n % 2 != 0:
        raise ValueError("Количество кусочков (n) должно быть четным для метода Симпсона")

    h = (b - a) / n
    integral_sum = func(a) + func(b)

    for i in range(1, n, 2):
        integral_sum += 4 * func(a + i * h)

    for i in range(2, n-1, 2):
        integral_sum += 2 * func(a + i * h)

    return integral_sum * h / 3

# Пример использования:
def example_function(x):
    return x**2

a = 0
b = 1
n = 1000

result = integrate_simpsons_rule(example_function, a, b, n)
print("Приближенное значение определенного интеграла:", result)
