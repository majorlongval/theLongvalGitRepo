"""The Snake Game. Version 0.3 beta
Built for the Udemy 100 days of Python code
Copyleft 2020 mlongval@gmail.com"""

# 07.12.2020: fixed speed and wall
# TODO:
# add "add_food"
# add "check_for_collision_with_food

##################################################
# Imports
from turtle import Turtle, Screen
from time import sleep
from random import randint
from typing import NewType

##################################################
# Setup and Globals

# screen setup
the_screen = Screen()
the_screen.screensize(300, 300)
size_x = the_screen.screensize()[0]
size_y = the_screen.screensize()[1]
the_screen.bgcolor("black")
the_screen.setup(width=1.0, height=1.0, startx=None, starty=None)

# globals
game_is_on = True
turtle_list = list()
current_heading = 0
max_snake_length = 4  # initialize to this value


##################################################
# Function definitions
def reset_game():
    global game_is_on
    global turtle_list
    global current_heading
    global max_snake_length
    game_is_on = True
    for turtle in turtle_list:
        turtle.hideturtle()
    turtle_list = list()
    current_heading = 0
    max_snake_length = 4  # initialize to this value
    run_game()


def turn_left():
    global current_heading
    current_heading += 90


def turn_right():
    global current_heading
    current_heading += -90


def detect_collision_with_self():
    global game_is_on
    global turtle_list
    for turtle in turtle_list[:-1]:
        if turtle.pos() == turtle_list[-1].pos():
            print("Crash into self")
            game_is_on = False


def detect_collision_with_wall():
    global game_is_on
    global turtle_list
    test_x = int(abs(turtle_list[-1].xcor())) >= the_screen.screensize()[0]
    test_y = int(abs(turtle_list[-1].ycor())) >= the_screen.screensize()[1]
    if test_x or test_y:
        print("Crash into wall")
        #print(f"X: {turtle_list[-1].pos()[0]}")
        #print(f"Y: {turtle_list[-1].pos()[1]}")
        game_is_on = False


def draw_outline():
    # This just draws the outline of the game board.
    global the_screen
    the_screen.tracer(5)
    timmy = Turtle()
    timmy.hideturtle()
    timmy.pencolor("blue")
    timmy.penup()
    timmy.goto(size_x, size_y)
    timmy.pendown()
    timmy.setheading(270)
    timmy.forward(size_y * 2)
    timmy.setheading(180)
    timmy.forward(size_x * 2)
    timmy.setheading(90)
    timmy.forward(size_y * 2)
    timmy.setheading(0)
    timmy.forward(size_x * 2)
    the_screen.update()
    sleep(3)

def run_game():
    global turtle_list
    global current_heading
    global game_is_on
    turtle_shape = "square"
    turtle_vertex = 20
    turtle_list.append(Turtle(shape=turtle_shape))
    turtle_list[0].penup()
    turtle_list[0].color("white")
    current_heading = turtle_list[0].heading()
    game_is_on = True
    while game_is_on:
        the_screen.tracer(500)
        turtle_list.append(turtle_list[-1].clone())
        turtle_list[-1].hideturtle()
        turtle_list[-1].setheading(current_heading)
        turtle_list[-1].forward(turtle_vertex)
        turtle_list[-1].showturtle()
        the_screen.update()

        if len(turtle_list) > max_snake_length:
            turtle_list[0].hideturtle()
            turtle_list.pop(0)

        detect_collision_with_self()
        detect_collision_with_wall()
        sleep(0.125)
# end run_game()


##################################################
# Main part of program

the_screen.onkey(key="Left", fun=turn_left)
the_screen.onkey(key="Right", fun=turn_right)
the_screen.onkey(key="r", fun=reset_game)
the_screen.onkey(key="q", fun=exit)
the_screen.listen()
draw_outline()
reset_game()
the_screen.exitonclick()
