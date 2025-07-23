# 3b - Draw a filled blue square
import turtle

t = turtle.Turtle()
t.fillcolor("blue")
t.begin_fill()
for _ in range(4):
    t.forward(75)
    t.right(90)
t.end_fill()
turtle.done()