#Yevhenii Stavytskiy HomeWork4
x = 0
while(x != 1):
        i = 0
        try :
            year = input("\n\n\n\nWrite number of year or end if you want to stop: ")
            if (year == "end"):
                print("Thank you for using the program!")
                x = 1
            else:
                year = int(year) #here can be exception
                if(year > 0):
                    while(i != 1):
                        try:
                            month = input("\nWrite number of month: ")
                            month = int(month) #here can be exception
                            if(month > 0 and month <= 12):
                                match month:
                                    case 1:
                                        print("\nJanuary - 31 days")
                                    case 2:
                                        if(year % 4 == 0):                          
                                            print("\nFebruar - 29 days and year is leap")
                                        else:
                                            print("\nFebruar - 28 days and year is not leap")
                                    case 3:
                                        print("\nMarch - 31 days")
                                    case 4:
                                        print("\nApril - 30 days")
                                    case 5:
                                        print("\nMay - 31 days")
                                    case 6:
                                        print("\nJune - 30 days")
                                    case 7:
                                        print("\nJuly - 31 days")
                                    case 8:
                                        print("\nAugust - 30 days")
                                    case 9:
                                        print("\nSeptember - 31 days")
                                    case 10:
                                        print("\nOctober - 30 days")
                                    case 11:
                                        print("\nNovember - 31 days")
                                    case 12:
                                        print("\nDecember - 30 days")
                                i = 1                                
                            elif(month > 12):
                                print("\nMonth can be more than 12")
                            elif(month < 1):
                                print("\nMonth can be less than 1")
                        except:
                             print("\nInvalid input, write number! ")
                elif(year < 1):
                    print("\nYear can`t be negative or 0")
        except :
            print("\nInvalid input, write number! ")


