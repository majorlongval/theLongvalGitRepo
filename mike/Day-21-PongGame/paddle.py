from turtle import Turtle
from turtle import Screen
from typing import List


# Paddle = List[Turtle]


class Paddle(Turtle):
    def __init__(self, screen: Screen, col: int, length: int = 4, name: str = "paddle"):
        super().__init__()

        self.screen = screen
        self.name = name

        self.length = length
        self.hideturtle()
        self.goto(col, 0)
        self.shape(name="square")
        self.setheading(270)
        self.color("white")
        self.penup()
        self.turtlesize(stretch_wid=1, stretch_len=5)
        self.showturtle()


        self.screen.update()

    def __str__(self):
        return self.name

    def move_down(self):
        self.forward(20)

    def move_up(self):
        self.backward(20)
