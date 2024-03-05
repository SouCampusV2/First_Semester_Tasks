filehandler = open("urls.txt")

for line in filehandler:
    urlFind = line.find("-") + 1
    name = line[urlFind:]
    print("Surname is:", name.capitalize())