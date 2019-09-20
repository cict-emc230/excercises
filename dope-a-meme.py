import turtle
import random

colors = ['#7D5D99', '#FF6F61', '#D5D717', '#A32857', '#0084A1', '#EE6D8A']

my_turtle = turtle.Turtle()
my_turtle2 = turtle.Turtle()

my_turtle.speed(0.5)

my_turtle.pensize(5)
my_turtle.penup()
my_turtle.setposition(-80, -150)
my_turtle.pendown()


def drawACurvedLine(count, angle, length, direction):
    for i in range(count):
        my_turtle.pencolor(colors[random.randrange(len(colors))])
        if direction == "left":
            my_turtle.forward(length)
            my_turtle.left(angle)
            my_turtle.forward(length)
        else:
            my_turtle.forward(length)
            my_turtle.right(angle)
            my_turtle.forward(length)


my_turtle2.pensize(5)
my_turtle2.penup()
my_turtle2.setposition(-70, 43)
my_turtle2.pendown()
my_turtle2.circle(5)
my_turtle2.circle(7)

my_turtle2.penup()
my_turtle2.setposition(0, 28)
my_turtle2.pendown()
my_turtle2.circle(5)
my_turtle2.circle(7)

# =========Body============

my_turtle.right(-90)
drawACurvedLine(3, 10, 5, "left")
my_turtle.right(-45)
drawACurvedLine(16, 10, 10, "right")
drawACurvedLine(5, 4, 8, "right")
drawACurvedLine(4, 9, 8, "right")
drawACurvedLine(14, 8, 8, "right")
drawACurvedLine(5, 10, 5, "left")

# ============End of Body============

# ============Left Eye============

my_turtle.penup()
my_turtle.setposition(-110, 40)
my_turtle.pendown()
my_turtle.right(180)
drawACurvedLine(5, 10, 3, "right")
drawACurvedLine(5, 10, 3, "right")
my_turtle.right(-290)
drawACurvedLine(8, 13, 4, "right")


# ============End of Left Eye============

# ============Right Eye============

my_turtle.penup()
my_turtle.setposition(0, 40)

my_turtle.pendown()
my_turtle.right(150)
drawACurvedLine(5, 10, 3, "right")
drawACurvedLine(5, 10, 3, "right")
my_turtle.right(-290)
drawACurvedLine(8, 13, 4, "right")

# ============End of Right Eye============


turtle.done()
