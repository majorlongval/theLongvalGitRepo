import colorgram
import turtle
import random

hirst_colors = colorgram.extract("hirst1.jpg", 50)

# process the colors to eliminate the really unsaturated (pale) ones
saturated_colors = list()
for color in hirst_colors:
    if color.hsl.s > 75:
        saturated_colors.append(color)

screen = turtle.Screen()
screen.colormode(255)
sw = screen.screensize()[0]
sh = screen.screensize()[1]

timmy = turtle.Turtle()
timmy.speed("fastest")
timmy.penup()
timmy.hideturtle()

tx = -1 * sw    # initial x position for turtle
ty = -1 * sh    # initial y position for turtle
x_offset = 115  # kludge to offset the spot onto the screen at right place
y_offset = 50

for _ in range(11):
    for _ in range(12):
        timmy.setposition(tx + x_offset,ty + y_offset)
        timmy.dot(30,random.choice(saturated_colors).rgb)
        tx += 50
    tx = -1 * sw
    ty += 50

screen.exitonclick()