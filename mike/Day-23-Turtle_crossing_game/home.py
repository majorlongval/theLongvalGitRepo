from turtle import Turtle
from turtle import Screen
from player import Player

COLLISION_DISTANCE = 10


class Home(Turtle):
    x: int
    y: int
    vacancy: bool

    def __init__(self, screen: Screen, x: int, y: int):
        super(Home, self).__init__()
        self.screen = screen
        self.new(x, y)

    def new(self, x: int, y: int):
        self.x = x
        self.y = y
        self.hideturtle()
        self.setheading(90)
        self.penup()
        self.goto(self.x, self.y)
        self.shape("square")
        self.shapesize(stretch_len=3, stretch_wid=3)
        self.color("green")
        self.vacancy = True
        self.showturtle()

    def collision(self, player: Player):
        if abs(self.distance(player.pos())) < COLLISION_DISTANCE:
            self.shape("turtle")
            self.vacancy = False
            return True
        else:
            return False