#Yevhenii Stavytskiy Practice4
x = 0
while(x != 1):
    try:
        customers = input("Write the number of customers or end to stop: ")
        if(customers == "end"):
            print("Thank you for using us!")
            break
        else:
            customers = int(customers)
            i = 1
            sum = 0
            while(i <= customers):
                if(i % 2 != 0):
                    sum = sum + i
                    i = i + 1
                else:
                    i = i + 1
            print("You need ", sum, " flowers")
    except:
        print("Wrong input! Write number!")