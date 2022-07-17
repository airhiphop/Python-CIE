import turtle
turtle.color('black', 'black')
head = 0
for i in range(4):
    if i % 2 == 1:
        turtle.begin_fill()
    turtle.setheading(head)
    for j in range(4):
        turtle.fd(100)
        turtle.left(90)
    head += 90
    if i % 2 == 1:
        turtle.end_fill()
turtle.hideturtle()
    
        