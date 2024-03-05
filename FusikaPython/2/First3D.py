import math

def cartesian_to_cylindrical(x, y, z):
    try:
        # Находим радиус (расстояние от начала координат до проекции точки на плоскость XY)
        r = math.sqrt(x**2 + y**2)

        # Находим азимут (угол в радианах)
        if x == 0:
            azimuth = math.pi / 2 if y > 0 else -math.pi / 2 if y < 0 else 0
            # Если y > 0, то угол azimuth устанавливается равным π/2 (90 градусов).
            # Если y < 0, то угол azimuth устанавливается равным -π/2 (-90 градусов).
            # Если y равно 0, то угол azimuth устанавливается равным 0.
        else:
            azimuth = math.atan2(y, x)

        # Находим высоту (координата z)
        height = z
        
        return r, azimuth, height

    except ValueError:
        raise ValueError("Ошибка: Введите числовые значения для координат x, y и z.")

def cylindrical_to_cartesian(r, azimuth, height):
    try:
        # Находим x и y из цилиндрических координат
        x = r * math.cos(azimuth)
        y = r * math.sin(azimuth)

        # Координата z остается неизменной
        z = height

        return x, y, z

    except ValueError:
        raise ValueError("Ошибка: Введите числовые значения для радиуса, азимута и высоты.")

try:
    # Ввод декартовых координат (x, y, z)
    x = float(input("Введите x: "))
    y = float(input("Введите y: "))
    z = float(input("Введите z: "))

    # Преобразование в цилиндрические координаты из декартовой
    cylindrical_coordinates = cartesian_to_cylindrical(x, y, z)
    print("Цилиндрические координаты:")
    print("Радиус (r):", cylindrical_coordinates[0])
    print("Азимут (в радианах):", cylindrical_coordinates[1])
    print("Высота (z):", cylindrical_coordinates[2])

    # Преобразование обратно в декартовы координаты из цилиндрических
    cartesian_coordinates = cylindrical_to_cartesian(*cylindrical_coordinates)
    print("\nОбратное преобразование в декартовы координаты:")
    print("x:", cartesian_coordinates[0])
    print("y:", cartesian_coordinates[1])
    print("z:", cartesian_coordinates[2])

except:
    print("Ошибка!")

