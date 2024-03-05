list = [5, 2, 1, 4, 3]
for i in range(len(list)):
    for j in range(i+1):
        if list[j] > list[i]:
            temp = list[i]
            list[i] = list[j]
            list[j] = temp

            
print(list)