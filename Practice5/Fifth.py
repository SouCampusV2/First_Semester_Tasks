#Yevhenii Stavytskiy Practice5
def convertor(cents):
    euros = cents // 100
    cents_remaining = cents % 100

    if euros == 0:
        if cents_remaining == 1:
            print(cents_remaining, " cent")
        else:
            print(cents_remaining, " cents")
    elif cents_remaining == 0:
        if euros == 1:
            print(euros, " euro")
        else:
            print(euros, " euros")
    else:
        if euros == 1:
            print(euros, " euro and", cents_remaining, " cents")
        else:
            print(euros, " euros and", cents_remaining, " cents")

try:
    cents = int(input("Please enter the number: "))
    if cents < 0:
        print("Please enter a non-negative number of cents.")
    else:
        convertor(cents)
except:
    print("Invalid input. Please write a valid number of cents.")
