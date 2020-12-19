from turtle import Turtle
from turtle import Screen
from random import randint


class Car(Turtle):
    def __init__(self, screen: Screen, direction: int = 0):
        super(Car, self).__init__()
        self.hideturtle()
        self.screen = screen
        self.setheading(direction)
        self.penup()
        self.shape("square")
        self.speed("fastest")
        self.shapesize(stretch_wid=2, stretch_len=3)
        self.y = 40 * randint(-5,5)
        self.x = 20 + (40 * randint(-14,14))

        self.min_x = -600
        self.max_x = 600
        self.goto(self.x, self.y)
        self.showturtle()

    def move(self):
        self.screen.tracer(0)
        self.forward(20)
        if self.xcor() > self.max_x:
            self.hideturtle()
            self.goto(self.min_x, self.y)
            self.showturtle()
        self.screen.update()