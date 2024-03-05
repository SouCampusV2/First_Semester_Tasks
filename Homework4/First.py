#Yevhenii Stavytskiy HomeWork4
i = 1
try:
    x = (int(input("Write the number that you want to multiply: ")))
    while(i < 10):
        print(x, "*", i, "= ", x * i)
        i = i + 1
except:
    print("Enter a number please.")