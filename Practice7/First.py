array = []
arraySquare = []
sum = 0
maxA = 0
minA = 0
numbers = 0

while True:
    try:
        a = input("Please write number, or Done if that`s all: ")
        if(a == "Done"):
            break
        a = int(a)
        array.append(a)
    except:
        print("Write right number!")

for i in array:
    sum = sum + i
    if(i % 2 == 0):
        numbers += 1
    arraySquare.append(i*i)

maxA = max(array)
minA = min(array)

print("Maximum = ", maxA)
print("Minimum = ", minA)
print("Even numbers = ", numbers)
print("Sum = ", sum)
print("Square arraay = ", arraySquare)