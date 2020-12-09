from turtle import Turtle, Screen
import time
from snake import Snake
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('My snake game')
screen.tracer(0)


# snake = []
snake_speed = 10
# # Initializing the game
# default_width = 20
# number_of_starting_segments = 3
# for i in range(0, number_of_starting_segments):
#     temp_segment = Turtle(shape='square')
#     temp_segment.color('white')
#     temp_segment.penup()
#     temp_segment.setx(-default_width*i)
#     snake.append(temp_segment)

snake = Snake()

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(1/snake_speed)

    snake.move()
    # time.sleep(1/snake_speed)
    # inv_snake = snake[::-1]
    # for i, seg in enumerate(inv_snake[:-1]):
    #     seg.goto(x=inv_snake[i+1].xcor(), y=inv_snake[i+1].ycor())
    #
    # snake[0].left(90)
    # snake[0].forward(20)


screen.exitonclick()

