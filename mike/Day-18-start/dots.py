from turtle import Turtle, Screen
from random import randrange
import random

the_screen = Screen()
tim = Turtle()
vertex = 30
the_screen.colormode(255)

def rand_color():
    red = randrange(255)
    green = randrange(255)
    blue = randrange(25)
    return (red, green, blue)

def rand_angle(n):
    the_list = []
    for i in range(n):
        the_list.append((360/n)*i)
    return random.choice(the_list)

tim.hideturtle()
tim.pensize(30)
tim.speed("fastest")
while True:
    tim.pencolor(rand_color())
    tim.pendown()
    tim.forward(1)
    tim.penup()
    tim.back(1)
    tim.right(rand_angle(4))
    tim.forward(vertex)



the_screen.exitonclick()

