#Yevhenii Stavytskiy HomeWork5
yourUrl = input("Please enter url: ")
urlFind = yourUrl.find("-") + 1
name = yourUrl[urlFind:]
print("Surname is: ", name.capitalize())