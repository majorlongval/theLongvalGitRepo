from turtle import Screen, Turtle
import time
from paddle
# Defining the screen of the game
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)
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


def go_down():
    paddle.goto(paddle.xcor(), paddle.ycor() - 20)


def go_left():
    paddle.goto(paddle.xcor() - 20, paddle.ycor())


def go_right():
    paddle.goto(paddle.xcor() + 20, paddle.ycor())


screen.onkeypress(go_up, 'Up')
screen.onkeypress(go_down, 'Down')

game_is_on = True

while game_is_on:
    screen.update()

screen.exitonclick()


