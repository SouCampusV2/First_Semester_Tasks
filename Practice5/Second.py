#Yevhenii Stavytskiy Practice5
epin = input("Please write your Estonian Personal Identifications Number: ")
try:
    if(int(epin[0]) == 0):
        print("EPIN can't start from 0")
    elif(int(epin[0]) % 2 == 0):
        print("You are woman.")
    elif(int(epin[0]) % 2 != 0):
        print("You are man.")
except:
    print("Invalid input!")