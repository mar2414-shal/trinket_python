import turtle
t = turtle.Turtle()

t.penup()
t.goto(100,100)
t.pendown()
for i in range(4):
  t.forward(50)
  t.left(90)
t.penup()
t.goto(50,25)
t.pendown()
for i in range(4):
  t.backward(25)
  t.left(90)
