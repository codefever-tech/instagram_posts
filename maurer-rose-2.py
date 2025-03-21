import turtle
import math

t = turtle.Turtle()
t.speed(0)
turtle.bgcolor("black")
t.pencolor("cyan")
t.pensize(1)

n = 8 # no of petals
d = 137 # step size

for i in range(361):
    k = i * d
    r = 200 * math.sin(math.radians(n * k))
    x = r * math.cos(math.radians(k))
    y = r * math.sin(math.radians(k))
    t.goto(x, y)
    t.pendown()

turtle.done()
