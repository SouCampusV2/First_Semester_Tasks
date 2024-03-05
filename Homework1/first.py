#Yevhenii Stavytskiy Homework1
i = 1

print("If you want to stop program write \"end\"")   
while(i < 5) :
     celsium = input("Enter temparature in C: ")
     if (celsium.isnumeric() == True) :
        fahrenheit = ((int(celsium) * 9 / 5) + 32)
        i = 1
        print("\n Temparature in fahrenheit = ", fahrenheit)

     elif(celsium == "end") :
        i = 5
        print("\n\nThank you!\n\n")
        exit(0) 

     else :
        i = 1
        print("\nInvalid input\n")
        
#Yevhenii Stavytskiy Homework1   



