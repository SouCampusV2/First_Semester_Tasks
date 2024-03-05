def car_price(price, years):
    if years == 0:
        return round(price, 2)
    else:
        procent = 0.8
        newPrice = float(price) * procent
        return car_price(newPrice, int(years) - 1)
    
p = input("Write a price of car: ")
y = input("Write a year of car: ")

print(car_price(p,y))