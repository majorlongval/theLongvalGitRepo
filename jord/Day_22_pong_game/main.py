from turtle import Screen, Turtle
import time
from keyStateChecker import KeyStateChecker

# Defining the screen of the game
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")

paddle = Turtle()
paddle.shape("square")
paddle.color("white")
paddle.shapesize(stretch_wid=5, stretch_len=1)
paddle.penup()
paddle.goto(350, 0)

screen.listen()
time.sleep(0.005)

def go_up():
    paddle.goto(paddle.xcor(), paddle.ycor() + 20)


screen.onkey(go_up, "Up")
screen.exitonclick()


