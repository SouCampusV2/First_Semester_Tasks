X = [[1,2],
    [3,4]]

Y = [[5,6,7],
    [8,9,10]]

if(len(X[0]) == len(Y)):
    N =  len(X)
    M = len(Y[0])
    result = []
    for i in range(N):
        result.append([0]*M)

for i in range(len(X)):
   for j in range(len(Y[0])):
       for k in range(len(Y)):
           result[i][j] += X[i][k] * Y[k][j]

for r in result:
   print(r)