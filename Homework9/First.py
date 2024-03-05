def Average(a):
    sum = 0
    count = len(a)
    for i in a:
        sum += i
    return sum/count  
        
def Minprice(a):
    mini = min(a)
    return mini
try: 
    fl = open("food.txt")
except:
    print("Error, file was not founded, please download it!")
    exit(0)

fullList = []

for line in fl:
    fullList.append(line)

matrix = []

for i in fullList:
    array = []

    index1 = i.find(" -")
    index2 = i.find(",")

    array.append(i[1: index1])
    array.append(i[index1 + 1 + 2:index2])
    array.append(float(i[index2 + 1:]))

    matrix.append(array)

food = input("Please write what you want to eat: ")
priceList = []
errorList = 0

for i in range(len(matrix)):
    if(food == matrix[i][1]):
        print("You can have", matrix[i][1], "in",  matrix[i][0], "for", matrix[i][2])
        priceList.append(matrix[i][2])
    elif(food != matrix[i][1]):
        errorList += 1
if(errorList == len(matrix)):
    print("This dish is not served in restaurants of Narva.")
else:
    average = Average(priceList)
    print("\nAverage price is", average, "EUR.")
    minimal = Minprice(priceList)
    print("Minimal price is", minimal, "EUR.")
    print("Difference between minimum and average prices is", average - minimal,"EUR.")





