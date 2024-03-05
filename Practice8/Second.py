
import turtle
turtle.setup(800, 600)
turtle.bgcolor("red")
turtle.title("Exercise 2")
turtle.shape("turtle")
turtle.speed(10)
turtle.pensize(50)
turtle.color("white")

# Move left up
turtle.penup()
turtle.goto(-800/2, 600/2)
turtle.pendown()

#white red white red lines
for i in range(6):
    turtle.pendown()
    turtle.forward(800)
    turtle.back(800)
    turtle.penup()
    turtle.right(90)
    turtle.forward(100)
    turtle.left(90)

turtle.penup()
turtle.goto(-800/2, 600/2)
turtle.pendown()

turtle.color("blue")

size1 = 400
size2 = 250

#Draw blue square of USA flag
for i in range(6):
    turtle.forward(size1)
    turtle.right(90)
    turtle.forward(size2)
    turtle.right(90)
    turtle.forward(size1)
    turtle.right(90)
    turtle.forward(size2)
    turtle.right(90)
    size1 -= 40
    size2 -= 40

#to draw white stars
turtle.pensize(5)
turtle.color("white")

turtle.penup()
turtle.right(90)

size3 = 10
for i in range (5):
    turtle.goto((-800/2) + 20, (600/2) - 20)
    turtle.forward(size3)
    turtle.pendown()
    turtle.stamp()
    size3 += 50
    for j in range(7):
        turtle.penup()
        turtle.left(90)
        turtle.forward(50)
        turtle.right(90)
        turtle.pendown()
        turtle.stamp()
        turtle.penup()



turtle.exitonclick()