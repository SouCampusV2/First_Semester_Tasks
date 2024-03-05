#Yevhenii Stavytskiy Practice1
i = 0 #just to stop "while"

#I think that in this task I don`t need to ask Tester about currency that he want to change, 
# because we have only 2 currencies.

while(i != 1):
    try :
        amount = input("Input amount of money and then choose the currency: ")
        amount = float(amount) #here can be exception
        i = 1

    except :
        print("Invalid amount! ")
        i = 0

while(i != 0):

        currencies = input("Write currencie that you will want to get \"Euro\" or \"Dollar\": ")
        if(currencies == "Euro") : #dollar to euro
            amount = amount * 0.93
            i = 0
        elif(currencies == "Dollar"): #euro to dollar
            amount = amount * 1.07
            i = 0
        elif(currencies != "Euro" or "Dollar"): 
            print("Invalid input, try again. ")
            i = 1
            
print("You will get", amount, currencies, "\n Thank you!")

