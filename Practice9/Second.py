matrix = [[5,6,7], [8,9,10]]

for i in range(len(matrix)):
    print("row", i)
    for j in range (len(matrix[i])):
        print(matrix[i][j])

print("\n\n\n-----------------------------------\n\n\n")

for i in range(len(matrix[0])):
    print("col", i)
    for j in range (len(matrix)):
        print(matrix[j][i])