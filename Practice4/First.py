#Yevhenii Stavytskiy Practice4
a = 0
while(a != 1):
    mantra = input("Write your favorite mantra please or end if you want to stop: ")
    if(mantra == "end"):
        print("Thank you for using us!")
        a = 1
    else:
        try:
            x = int(input("Write how many times to repeat: "))
            i = 0
            while(i < x):
                print(mantra)
                i = i + 1
        except:
            print("Wrong input! Pleaase write number.")