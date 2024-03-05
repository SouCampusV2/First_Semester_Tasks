import matplotlib.pyplot as plt
import numpy as np

# Функция для вычисления спектральной светимости
def spectral_radiance(f, T):
    return f**3 / (np.exp(f/T) - 1)

# Шаг частоты
freq_range = np.arange(100, 20001, 100)

# Температуры
temperatures = [500, 1000, 1500, 2000, 2500]

# Построение графиков
plt.figure(figsize=(10, 6))

for T in temperatures:
    radiance_values = [spectral_radiance(f, T) for f in freq_range]
    plt.plot(freq_range, radiance_values, label=f'T={T}K')

plt.title('Зависимость спектральной светимости от частоты и температуры')
plt.xlabel('Частота, f')
plt.ylabel('Спектральная светимость, r')
plt.legend()
plt.grid(True)
plt.show()

# Поиск частоты fmax при максимальной светимости
fmax_values = []

for T in temperatures:
    radiance_values = [spectral_radiance(f, T) for f in freq_range]
    fmax = freq_range[np.argmax(radiance_values)]
    fmax_values.append(fmax)

# Построение графика зависимости T / fmax от температуры
plt.figure(figsize=(6, 6))
plt.plot(temperatures, np.divide(temperatures, fmax_values), marker='o')
plt.title('Проверка закона Вина: T / fmax = const')
plt.xlabel('Температура, T')
plt.ylabel('T / fmax')
plt.grid(True)
plt.show()

# Проверка закона Стефана–Больцмана
# Вычисление суммы значений спектральной светимости для каждой температуры
total_energy = [np.sum([spectral_radiance(f, T) for f in freq_range]) for T in temperatures]

# Построение графика зависимости суммы светимостей от T^4
plt.figure(figsize=(6, 6))
plt.plot(np.power(temperatures, 4), total_energy, marker='o')
plt.title('Проверка закона Стефана–Больцмана')
plt.xlabel('T^4')
plt.ylabel('Суммарная светимость')
plt.grid(True)
plt.show()