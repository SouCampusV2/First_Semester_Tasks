import datetime

fl = open("dates.txt")

birthyear_counts = {}

for line in fl:
    parts = line.strip().split('-')
    year, month, day = map(int, parts)
    date = datetime.datetime(year, month, day)   

    # Определяем год и увеличиваем счетчик в словаре
    if date.year in birthyear_counts:
        birthyear_counts[date.year] += 1
    else:
        birthyear_counts[date.year] = 1

# Сортируем словарь по количеству дней рождений с помощью лямбда функции. birthyear_counts.items() - список кортежей, в себе содержит год рождения и кол повторов
# reverse=True обеспечивает сортировку по убыванию.
# 
sorted_birthyears = dict(sorted(birthyear_counts.items(), key=lambda item: item[1], reverse=True))

# Выводим топ 3 годов, енумурейт возвращает значение и ключ - так удобно выводить год и кол повторений 
print("Top 3 birth years:")
for i, (birthyear, count) in enumerate(sorted_birthyears.items()):
    print(f"{i + 1}. Year {birthyear}: {count} times")
    if i + 1 == 3:
        break
