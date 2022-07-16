import turtle
turtle.penup()
turtle.goto(-100, -100)
turtle.pendown()

for i in range(4):
    turtle.fd(200)
    turtle.left(90)
    
turtle.pencolor('red')
x = -40
for i in range(3):
    turtle.penup()
    turtle.goto(x, 0)
    turtle.dot(20)
    turtle.pendown()
    x += 40
turtle.hideturtle()