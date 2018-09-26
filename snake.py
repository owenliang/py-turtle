import turtle

turtle.setup(1000, 1000, 0, 0)
turtle.mode('logo')

turtle.pensize(30)
turtle.color('green')

turtle.penup()
turtle.goto(-400, 0)
turtle.pendown()

turtle.setheading(45)

for i in range(1, 5):
    turtle.circle(-70, 360/4)
    turtle.circle(70, 360/4)
