fh = open("temps.txt")
arrayF = []
arrayC = []
average = 0

for line in fh:
    frht = ((float(line) * 9 / 5) + 32)
    arrayF.append(frht)
    arrayC.append(line)
    average += frht

print("Temparature from file in C: ", arrayC)
print("Temparature from file in F: ", arrayF)
print("Average temparature in F: ", average / len(arrayF))
print("Max temparature in F: ", max(arrayF))
print("Min temparature in F: ", min(arrayF))




    