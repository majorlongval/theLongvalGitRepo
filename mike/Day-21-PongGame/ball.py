from turtle import Turtle
from turtle import Screen
import random
from paddle import Paddle
from scoreboard import Score
from time import sleep

START_HEADINGS = [0, 180, 30, 45, 135, 150, 210, 225, 345, 315]
PADDLE_COLLISION_DISTANCE = 25

class Ball(Turtle):
    def __init__(self, screen: Screen, paddle1: Paddle, paddle2: Paddle, scoreboard: Score):
        super(Ball, self).__init__()
        self.paddle1 = paddle1
        self.paddle2 = paddle2
        self.scoreboard = scoreboard
        self.screen = screen
        self.new_ball()

    def new_ball(self):
        self.hideturtle()
        self.penup()
        self.color("white")
        self.shape(name="circle")
        self.goto(0, 0)
        self.setheading(random.choice(START_HEADINGS))
        print(f"Initial Heading: {self.heading()}")
        self.showturtle()

    def move(self):
        self.forward(20)
        self.wall_collision()
        self.backstop_collision()
        self.paddle_collision(self.paddle1)
        self.paddle_collision(self.paddle2)

    def wall_collision(self):
        if abs(self.ycor()) >= abs(self.screen.screensize()[1]):
            self.setheading(-1 * self.heading())
            print("Collision with wall")

    def backstop_collision(self):
        if abs(self.xcor()) >= abs(self.screen.screensize()[0]):
<<<<<<< HEAD
            self.setheading(180 - self.heading())
            if self.xcor() > 0:
                self.scoreboard.left_inc()
            else:
                self.scoreboard.right_inc()
=======
            if self.xcor() < 0:
                self.scoreboard.right_inc()
            else:
                self.scoreboard.left_inc()
>>>>>>> main
            self.scoreboard.update_scoreboard()
            self.new_ball()

    def paddle_collision(self, paddle: Paddle):
<<<<<<< HEAD
        self.screen.tracer(500)
        for segment in paddle:
            if self.distance(segment.pos()) < PADDLE_COLLISION_DISTANCE:
                self.setheading(180 - self.heading())
                print("Collision with paddle", paddle)
        self.screen.update()
=======
        print(self.xcor())
        if (abs(self.xcor()) > 350) and (paddle.distance(self.pos()) < 50):
            self.setheading(180 - self.heading())
            print("Collision with paddle", paddle)
>>>>>>> main
