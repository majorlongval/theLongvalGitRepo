from turtle import Turtle, Screen
from random import randint


screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(
    title="Place your bets", prompt="Which turtle will win? Enter a color: "
)
colors = ["red", "blue", "green", "yellow", "purple", "orange"]
starting_line = -230
finish_line = 230
starting_y = -90
turtle_list = list()
still_racing = True
for color in colors:
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(color)
    new_turtle.setposition(x=starting_line, y=starting_y)
    starting_y += 30
    turtle_list.append(new_turtle)

while still_racing:
    for friend in turtle_list:
        friend.forward(randint(1, 7))
        if friend.xcor() > finish_line:
            print(f"{friend.color()[0]} won")
            if friend.color()[0] == user_bet:
                print("You win!")
            else:
                print("You loose!")
            still_racing = False

screen.exitonclick()
