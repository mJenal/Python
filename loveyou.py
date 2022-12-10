import turtle

turtle.speed(5)
t = turtle.Turtle()
s = turtle.Screen()

def func():
    for i in range(200):
        turtle.right(1)
        turtle.forward(1)
        
s.bgcolor('black')
t.hideturtle()
t.goto(0,10)

t.pensize(3)
t.color('red')
t.begin_fill()
t.left(140)
t.forward(180)
t.circle(-90, 200)
t.setheading(60)
t.circle(-90, 200)
t.forward(178)
t.end_fill()

t.penup()
t.goto(-100,130)
t.pendown()
t.color('white')
t.write('I LOVE YOU', font=('Verdana',25,'bold'))

t.down()