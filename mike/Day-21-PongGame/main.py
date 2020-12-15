from turtle import Screen
from turtle import mainloop
from paddle import Paddle
from ball import Ball
from scoreboard import Score
from time import sleep

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
MOVE_DELAY = 0.125  # seconds

screen = Screen()
screen.bgcolor("black")
screen.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
score1 = Score(screen)
paddle1 = Paddle(screen=screen, col=370, name="Mike")
paddle2 = Paddle(screen=screen, col=-370, length=10, name="Jord")
ball1 = Ball(screen=screen, paddle1=paddle1, paddle2=paddle2, scoreboard=score1)
screen.onkeypress(key="j", fun=paddle1.move_down)
screen.onkeypress(key="k", fun=paddle1.move_up)
screen.onkeypress(key="f", fun=paddle2.move_down)
screen.onkeypress(key="d", fun=paddle2.move_up)
screen.onkeypress(key="q", fun=exit)
screen.ontimer(fun=ball1.move, t=1)
screen.listen()

while True:
    screen.tracer(0)
    ball1.move()
    sleep(MOVE_DELAY)
    screen.update()



