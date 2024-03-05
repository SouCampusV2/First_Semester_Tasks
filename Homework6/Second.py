filehandler = open("names.txt")
i = 1
for line in filehandler:
    print(i, line)
    i += 1
