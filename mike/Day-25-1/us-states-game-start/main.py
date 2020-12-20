from turtle import Turtle
import turtle
from turtle import Screen
import csv

# Screen Setup
image = 'blank_states_img.gif'  # source for the background
screen = Screen()
# screen.screensize(1200,1000)
screen.title("USA States Game")
turtle.addshape(image)
# there is a bug in the Turtle library ... I am getting a fullscreen
# dialog box over my map. I cannot find a way to avoid this.
#
# Setting this project aside and moving on to next one.
turtle.shape(image)

# Data Setup
useful_data = [None]
with open("50_states.csv") as fh:
    data = csv.reader(fh)
    for row in data:
        useful_data.append(row)

states = [row[0] for row in useful_data[2:]]
coords = [(row[1], row[2]) for row in useful_data[2:]]

# Text Input
# Having trouble here because on my version of Python I am getting
# a fullscreen popup, not a dialog box.
while True:
    user_input = turtle.textinput(prompt="State Name:", title="States Game").title()
    if user_input == "Exit":
        break
    if user_input in states:
        print(coords[states.index(user_input)])

screen.exitonclick()
