from turtle import Turtle
from turtle import Screen
from typing import List


# Paddle = List[Turtle]


class Paddle(List[Turtle]):

    def __init__(self, screen: Screen, col: int, length: int = 4):
        super().__init__()

        self.screen = screen
        self.length = length
        self.append(Turtle())
        head = self[0]
        self.screen.tracer(500)
        head.hideturtle()
        head.goto(col, 0)
        head.shape(name="square")
        head.setheading(270)
        head.color("white")
        head.penup()
        head.showturtle()
        for _ in range(self.length):
            self.append(self[-1].clone())
            self[-1].forward(20)
        self.screen.update()

    def move_down(self):
        self.screen.tracer(500)
        for segment in self:
            segment.forward(20)
        print("move down")
        self.screen.update()

    def move_up(self):
        self.screen.tracer(500)
        for segment in self:
            segment.backward(20)
        print("move up")
        self.screen.update()
