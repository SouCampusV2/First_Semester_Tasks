try:
    fl = open("Words.txt", 'r')
except:
    print("File was not found.")
    exit(0)
dictonar = {}
for line in fl:
    dictonar[line[0:line.find(":")]] = line[line.find(":") + 1 :len(line) - 1]

exitC = "123"
print("Wirte \"done\" to quit the program!")
while exitC != "done":

    newWord = input("Please write word that you want to translate from English into Ukranian: ")
    if newWord == "done":
        exitC = "done"
    else:
        if(newWord not in dictonar):
            meaning = input("This word is not in the dictionaries, please write meaning on Ukranian: ")
            dictonar[newWord] = meaning
                
        elif(newWord in dictonar):
            print("Your word means: ", dictonar[newWord])
            
        else:
            print("Error.")
          

with open('Words.txt', 'w') as file: 
        for word, meaning in dictonar.items(): 
            file.write(f"{word}: {meaning}\n")