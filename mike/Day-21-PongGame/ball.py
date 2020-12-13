from turtle import Turtle
from turtle import Screen
from random import randint


class Ball(Turtle):
    def __init__(self, screen: Screen):
        super(Ball, self).__init__()

        self.screen = screen
        self.screen.tracer(500)
        self.hideturtle()
        self.penup()
        self.color("white")
        self.shape(name="square")
        self.goto(0, 0)
        self.setheading(randint(0, 359))
        self.showturtle()
        self.screen.update()

    def move(self):
        self.screen.tracer(500)
        self.forward(20)
        self.wall_collision()
        self.screen.update()
        self.screen.ontimer(self.move, 25)

    def wall_collision(self):
        if abs(self.ycor()) >= abs(self.screen.screensize()[1] /2):
            # collision with a wall
            self.setheading(-180 - self.heading())