import colorgram
import turtle
import random

def rand_color(colors):
    return random.choice(colors).rgb


hirst_colors = colorgram.extract("hirst1.jpg", 15)

screen = turtle.Screen()
screen.colormode(255)
screen_width = screen.screensize()[0]
screen_height = screen.screensize()[1]
print(screen_width, screen_height)


timmy = turtle.Turtle()
timmy.hideturtle()
timmy.pensize(30)
timmy.speed("fastest")

vertex = 50
timmy.penup()
timmy.setx(-400)
timmy.sety(-300)

def plop():
    timmy.pencolor(random.choice(hirst_colors).rgb)
    timmy.pendown()
    timmy.forward(1)
    timmy.penup()
    timmy.backward(1)

sw = 400
sh = 300
tx = -1 * sw
ty = -1 * sh

for _ in range(220):
    timmy.setposition(tx,ty)
    plop()
    tx += 50
    if tx > sw:
        tx = -1 * sw
        ty += 50

screen.exitonclick()