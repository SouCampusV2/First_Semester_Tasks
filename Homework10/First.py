import datetime

fl = open("dates.txt")

dictor = {}

for line in fl:
    date = datetime.datetime(int(line[0:4]), int(line[5:7]), int(line[8:10]))
    numDay = date.weekday()
    match numDay:
        case 1:
            dictor[line] = "Monday"
        case 2:
            dictor[line] = "Tuesday"
        case 3:
            dictor[line] = "Wednesday"
        case 4:
            dictor[line] = "Thursday"
        case 5:
            dictor[line] = "Friday"
        case 6:
            dictor[line] = "Saturday"
        case 7:
            dictor[line] = "Sunday"
    
    
    
for line in dictor:
    print(line, dictor[line])

with open('datesWithDay.txt', 'w') as file: 
        for word, meaning in dictor.items(): 
            file.write(f"{word}: {meaning}\n")