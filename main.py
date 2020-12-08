from turtle import Turtle, Screen
from time import sleep
from random import randint
from typing import NewType

##################################################
# Setup and Globals
the_screen = Screen()
the_screen.bgcolor("black")
sizex = 300
sizey = 300
the_screen.screensize(sizex, sizey)
the_screen.setup(width=1.0, height=1.0, startx=None, starty=None)
turtle_shape = "square"
turtle_vertex = 20
turtle_list = list()
turtle_list.append(Turtle(shape=turtle_shape))
turtle_list[0].penup()
turtle_list[0].color("white")
current_heading = turtle_list[0].heading()
game_is_on = True
max_snake_length = 4  # initialize to this value
max = the_screen.screensize()
max_x = max[0]
max_y = max[1]


##################################################
# Function definitions


def turn_left():
    global current_heading
    current_heading += 90


def turn_right():
    global current_heading
    current_heading += -90


def detect_collision_with_self():
    global game_is_on
    global turtle_list
    # print(turtle_list[:-1])
    for current_turtle in turtle_list[:-1]:
        # print(f"Current: {current_turtle.pos()}")
        # print(f"Last: {turtle_list[-1].pos()}")
        if current_turtle.pos() == turtle_list[-1].pos():
            print("Crash")
            game_is_on = False


def detect_collision_with_wall():
    global game_is_on
    global turtle_list
    test_x = int(abs(turtle_list[-1].xcor())) >= the_screen.screensize()[0]
    test_y = int(abs(turtle_list[-1].ycor())) >= the_screen.screensize()[1]
    if test_x or test_y:
        print("Crash into wall")
        print(f"X: {turtle_list[-1].xcor()}")
        print(f"Y: {turtle_list[-1].ycor()}")
        print(f"{the_screen.screensize()}")
        game_is_on = False


def draw_outline():
    # This just draws the ouline of the game board.
    timmy = Turtle()
    timmy.hideturtle()
    timmy.pencolor("blue")
    timmy.penup()
    timmy.goto(max_x, max_y)
    timmy.pendown()
    timmy.setheading(270)
    timmy.forward(max_y * 2)
    timmy.setheading(180)
    timmy.forward(max_x * 2)
    timmy.setheading(90)
    timmy.forward(max_y * 2)
    timmy.setheading(0)
    timmy.forward(max_x * 2)


def place_food(current: Turtle = None) -> Turtle:
    # pick a random x and y cood
    if current is None:
        upper_limit_x = int(sizex / 40)
        upper_limit_y = int(sizey / 40)
        rand_x = randint(1, upper_limit_x) * 40
        rand_y = randint(1, upper_limit_y) * 40
        food = Turtle()
        food.hideturtle()
        food.shape("square")
        food.color("blue")
        food.penup()
        food.hideturtle()
        food.goto(x=rand_x, y=rand_y)
        food.showturtle()
        return food
    else:
        return current


def collision(set1, set2) -> bool:
    print(set1, set2)
    x1 = int(set1[0] / 10)
    y1 = int(set1[1] / 10)
    x2 = int(set2[0] / 10)
    y2 = int(set2[1] / 10)
    print(x1, y1, x2, y2)
    if x1 == x2 and y1 == y2:
        return True
    else:
        return False


def detect_collision_with_food(food: Turtle) -> bool:
    global game_is_on
    if collision(food.pos(), turtle_list[-1].pos()):
        print("food eaten")
        return True
    else:
        return False


# make sure they are not on the current snake

##################################################
# Main part of program

draw_outline()
the_screen.onkey(key="Left", fun=turn_left)
the_screen.onkey(key="Right", fun=turn_right)
the_screen.listen()
food = None
while game_is_on:
    food = place_food(food)
    turtle_list.append(turtle_list[-1].clone())
    turtle_list[-1].hideturtle()
    turtle_list[-1].setheading(current_heading)
    turtle_list[-1].forward(turtle_vertex)
    turtle_list[-1].showturtle()

    if len(turtle_list) > max_snake_length:
        turtle_list[0].hideturtle()
        turtle_list.pop(0)

    detect_collision_with_self()
    detect_collision_with_wall()
    if detect_collision_with_food(food):
        food.hideturtle()
        food = place_food(None)
        max_snake_length += 1

the_screen.exitonclick()
