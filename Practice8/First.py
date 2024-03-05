from turtle import *
 
bcolor = input("Please write a color of backhround: ")
lcolor = input("Please write a color of line: ")
size = int(input("Please write size of pen: "))

title("Exercise 1")
setup(800, 800)  
bgcolor(bcolor)
color(lcolor)
pensize(size)

forward(300)
left(90)
forward(200)
left(90)
forward(300)
left(90)
forward(200)

exitonclick()