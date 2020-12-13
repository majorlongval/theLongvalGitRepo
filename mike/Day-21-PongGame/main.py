from turtle import Screen
from turtle import mainloop
from paddle import Paddle
from ball import Ball
from time import sleep

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


screen = Screen()
screen.bgcolor("black")
screen.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
ball1 = Ball(screen=screen)
paddle1 = Paddle(screen=screen, col=370)
paddle2 = Paddle(screen=screen, col=-370, length=10)
screen.onkeypress(key="j", fun=paddle1.move_down)
screen.onkeypress(key="k", fun=paddle1.move_up)
screen.onkeypress(key="f", fun=paddle2.move_down)
screen.onkeypress(key="d", fun=paddle2.move_up)
screen.onkeypress(key="q", fun=exit)
screen.ontimer(fun=ball1.move, t=5)
screen.listen()

mainloop()