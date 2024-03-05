import math

def calculate_time(x, a, b, v1, v2):
    time_to_C = math.sqrt(a**2 + x**2) / v1
    time_to_B = math.sqrt((b**2) + (a - x)**2) / v2
    return time_to_C + time_to_B

def law_of_refraction(x, a, b, n1, n2):
    alpha = math.atan(x/a)
    beta = math.atan((b - x)/(math.sqrt((b**2) + (a - x)**2)))
    
    # Проверка закона преломления
    if math.isclose(math.sin(alpha) / math.sin(beta), n2 / n1):
        return n1 * math.sin(alpha), n2 * math.sin(beta)
    else:
        raise ValueError("Закон преломления не выполняется!")

# Исходные данные
a = 3  # расстояние от A до границы раздела
b = 4  # расстояние от B до границы раздела
v1 = 1  # скорость света в первой среде
v2 = 1.5  # скорость света во второй среде
n1 = 1.5  # показатель преломления для первой среды
n2 = 2.0  # показатель преломления для второй среды

# Создание массива значений x для расчета времени
x_values = [i/10 for i in range(int((a + b)*10) + 1)]

# Рассчет времени и функций для каждого значения x
time_values = [calculate_time(x, a, b, v1, v2) for x in x_values]
f1_values, f2_values = zip(*[law_of_refraction(x, a, b, n1, n2) for x in x_values])

# Нахождение кратчайшего маршрута
optimal_x = x_values[time_values.index(min(time_values))]
min_time = min(time_values)

# Вывод результатов
print(f"Кратчайший маршрут (по времени) находится при x = {optimal_x}")
print(f"Минимальное время прохождения света: {min_time} сек")
