from turtle import Turtle, Screen

screen = Screen()
screen_w = 500
screen_h = 400
screen.setup(width=500, height=400)

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


setup_game()







screen.exitonclick()
