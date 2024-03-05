def monthcalc(month):
    try:
                        month = int(month) #here can be exception
                        if(month > 0 and month <= 12):
                            match month:
                                case 1:
                                    print("\nJanuary - 31 days")
                                case 2:                     
                                    print("\nFebruar - 29 days if year is leap")
                                    print("\nFebruar - 28 days if year is not leap")
                                case 3:
                                    print("\nMarch - 30 days")
                                case 4:
                                    print("\nApril - 31 days")
                                case 5:
                                    print("\nMay - 30 days")
                                case 6:
                                    print("\nJune - 31 days")
                                case 7:
                                    print("\nJuly - 30 days")
                                case 8:
                                    print("\nAugust - 31 days")
                                case 9:
                                    print("\nSeptember - 30 days")
                                case 10:
                                    print("\nOctober - 31 days")
                                case 11:
                                    print("\nNovember - 30 days")
                                case 12:
                                    print("\nDecember - 31 days")
                            i = 1                                
                        elif(month > 12):
                            print("\nMonth can be more than 12")
                        elif(month < 1):
                            print("\nMonth can be less than 1")
    except:
        print("\nInvalid input, write number! ")

def differentCalc(): 
    priceProduct = input("\nWrite price of the  product: ")

    pricePerMonth1 = float(input("\nWrite what is the monthly payment on the first installment plan?: "))
    timeToPay1 = float(input("\nWrite how many months does the first installment plan last?: "))

    pricePerMonth2 = float(input("\nWrite what is the monthly payment on the second installment plan?: "))
    timeToPay2 = float(input("\nWrite how many months does the second installment plan last?: "))

    price1 = float(pricePerMonth1 * timeToPay1) #how much pay in the result for the first plan
    price2 = float(pricePerMonth2 * timeToPay2) #how much pay in the result for the secodn plan

    #logic which is better
    if(price1 > price2):
         print("Second plan is better!")
         return price1 - price2
    elif(price2 > price1):
         print("First plan is better!")
         return price2 - price1
    elif(price1 == price2):
        print("They are equal!")
        return price1 - price2
    else:
         print("Error 404")

x = int(input("Write which task you want to test: 1 or 2: "))
if(x == 1):
    monthToCalc = input("\nWrite number of month: ")
    monthcalc(monthToCalc)
elif(x == 2):
     result = differentCalc()
     print("The different of plans is = ", result)
     
