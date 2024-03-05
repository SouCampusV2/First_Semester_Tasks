def number_of_coins(safe_number):
    if safe_number == 1:
        return 1
    else:
        return safe_number + number_of_coins(safe_number - 1)

print(number_of_coins(11)) 

