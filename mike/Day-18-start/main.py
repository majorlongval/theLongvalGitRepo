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
tim.pensize(2)
tim.speed("fastest")

step = 15
for _ in range(0,360, step):
    tim.pencolor(rand_color())
    tim.circle(150)
    tim.left(step)


the_screen.exitonclick()
