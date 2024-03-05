#Yevhenii Stavytskiy Practice5
fName = input("Please write your first name: ")
lName = input("Please write your last name: ")
mail = input("Please write your e-mail: ")
occupation = input("Please write your occupation: ")

lenOfTable = len(fName) + len(lName) + len(mail) + 4 + 8

print("+" + ("-" * (lenOfTable - 2)) + "+")
print("|" + (" " * (lenOfTable - 2)) + "|")
print("|" + (fName + " " + lName + " - " + mail).center(lenOfTable - 2, " ") + "|")
print("|" + (" " * (lenOfTable - 2)) + "|")
print("|" + (occupation.center(lenOfTable - 2, " ")) + "|")
print("|" + (" " * (lenOfTable - 2)) + "|")
print("+" + ("-" * (lenOfTable - 2)) + "+")
