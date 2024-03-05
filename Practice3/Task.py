def calculation(dist):
    screenDiagonal = dist * 100 * 0.39 / 2.5
    screenDiagonal = round(screenDiagonal)
    return screenDiagonal

try:
    x = input("Write the distance from the screen in meters: ")
    x = float(x) #here can be an error
    if(x > 0):
        result = calculation(x)
        print("Diagonal must be ~", result, "duim")
    elif(x <= 0):
        print("Write a right number please!")
    else: 
        print("Error")
except:
    print("Write a number please!")