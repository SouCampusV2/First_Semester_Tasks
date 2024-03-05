#Yevhenii Stavytskiy HomeWork5
name = input("Write your name please: ")
name.capitalize()
grades = input("Write your grades please: ")
grades = grades.upper()
count = len(grades)
secondGrade = grades[1]

countAB = grades.count("A") + grades.count("B")

print("Hello ", name, ", your grades are: ", grades)
print("You have ", count, " grades!")
print("Your grade for second course is: ", secondGrade)
print("The number of A's and B's is: ", countAB)