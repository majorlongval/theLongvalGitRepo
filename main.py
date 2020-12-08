from turtle import Turtle, Screen
import random
screen = Screen()
screen_w = 500
screen_h = 400
screen.setup(width=screen_w, height=screen_h)

user_bet = screen.textinput(title='Make your bet', prompt="Which turtle will win the race?")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]


def setup_game():
    set_of_turtles = []
    for color, i in zip(colors, range(0, len(colors))):
        tmp_turtle = Turtle(shape='turtle')
        tmp_turtle.color(color)
        tmp_turtle.penup()
        tmp_turtle.goto(x=-230, y=(-screen_h/(2*len(colors)) + (i-2)*screen_h/(2*len(colors))))
        set_of_turtles.append(tmp_turtle)
    return set_of_turtles


set_of_turtles = setup_game()
finished = False
while not finished:
    for turtle in set_of_turtles:
        turtle.forward(random.randint(0, 10))
        if turtle.xcor() >= 230:
            winner_color = turtle.color()[0]
            print(f"the {winner_color} turtle has won")
            if winner_color == user_bet:
                print("You won !!!!! Bravo")
            else:
                print("You lost, give me your money...")
            finished = True
            break



screen.exitonclick()
