filehandler = open("data.txt")
sum = 0
for line in filehandler:
    try:
        number = int(line)
        print("*" * number)
        sum += number
    except:
        print("None")
print("* in total = ", sum)
