import math

def coordinates():
    x = float(input("Please write x coordinate: "))
    y = float(input("Please write y coordinate: "))
    return x, y

def distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def closest_points(num_points):
    points = []
    for i in range(1, num_points + 1):
        print("Please write coordinates for", i, "point:")
        points.append(coordinates())
    #бесконечное положительное число, юзается для сравнения
    min_distance = float('inf')
    closest_pair = ()

    for i in range(num_points - 1):
        for j in range(i + 1, num_points):
            dist = distance(points[i][0], points[i][1], points[j][0], points[j][1])
            if dist < min_distance:
                min_distance = dist
                closest_pair = (i + 1, j + 1)

    print("Points", closest_pair[0], closest_pair[1], "are the closest to each other.")


closest_points(4)
