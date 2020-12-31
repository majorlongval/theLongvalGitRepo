from turtle import Turtle
from turtle import Screen

STEP_LENGTH = 60


class Player(Turtle):
    def __init__(self, screen: Screen):
        super().__init__()
        self.screen = screen
        self.screen.tracer(1)
        self.new_player()

    def new_player(self):
        self.penup()
        self.hideturtle()
        self.color("blue")
        self.shape("turtle")
        self.goto(x=0, y=-340)
        self.setheading(90)
        self.shapesize(stretch_wid=2, stretch_len=2)
        self.showturtle()

    def go_down(self):
        self.setheading(270)
        self.forward(STEP_LENGTH)

    def go_up(self):
        self.setheading(90)
        self.forward(STEP_LENGTH)

    def go_left(self):
        self.setheading(180)
        self.forward(STEP_LENGTH)

    def go_right(self):
        self.setheading(0)
        self.forward(STEP_LENGTH)