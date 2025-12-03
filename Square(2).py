import turtle
t = turtle.Turtle()

def square(size):
  for i in range(4):
    t.forward(size)
    t.right(90)
    
square(150)
square(100)
square(50)
