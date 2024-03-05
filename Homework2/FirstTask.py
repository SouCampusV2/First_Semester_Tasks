#Yevhenii Stavytskiy Practice2
x = 0
while(x != 1):
        try :
            point = input("Write your nubmer of points: ")
            point = float(point) #here can be exception
            if(point < 0):
                print("Your point can`t be negative")
                x = 0
            elif(point >= 66 and point <= 100):
                print("Your mark is A")
                x = 1
            elif(point <= 65 and point >= 30):
                print("Your mark is B")
                x = 1
            elif(point <= 29 and point >= 1):
                print("Your mark is C")   
                x = 1
            elif(point == 0):
                print("Your point can`t be 0")
                i = 0
            elif(point > 100):
                print("Your point can`t be more than 100")
                i = 0
            else:
                print("Error")
                i = 0
        except :
            print("Invalid input, write number! ")
            x = 0
