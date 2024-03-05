fh = open("Dates.txt")
months = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
for line in fh:
    monthD = int(line[3:5])
    print("Days in month:", months[monthD])
