"""OOP version of Snake Game"""
##################################################
# Imports and type definitions
from turtle import Turtle
from turtle import Screen
from time import sleep
from typing import List
Segments = List[Turtle]


class Snake(Segments):
    segment_len: int
    max_len: int
    heading: int

    def __init__(self, our_screen: Screen):
        super().__init__()
        self.screen = our_screen
        self.reset()

    def reset(self):
        for segment in self:
            segment.hideturtle()
        self.clear()
        self.segment_len = 20
        self.max_len = 12
        self.heading = 0
        head = Turtle(shape='square')
        head.penup()
        head.color('white')
        head.setheading(self.heading)
        self.append(head)

    def current_heading(self) -> int:
        return int(self[-1].heading())

    def turn_left(self):
        self[-1].setheading(self.current_heading() + 90)

    def turn_right(self):
        self[-1].setheading(self.current_heading() - 90)

    def move(self):
        self.screen.tracer(500)
        self.append(self[-1].clone())
        self[-1].forward(self.segment_len)
        if len(self) > self.max_len:
            self.delete_segment()
        self.screen.update()
        self.self_collision_detect()

    def delete_segment(self, segment: int = 0):
        self[segment].hideturtle()
        self.pop(segment)

    def wall_collision_detect(self):
        pass

    def self_collision_detect(self):
        position_list = [segment.position() for segment in self]
        int_position_list = [(int(x[0]), int(x[1])) for x in position_list]
        if len(int_position_list) > len(set(int_position_list)):
            print("collision with self")
            self.reset()

    def food_collision_detect(self):
        pass

    def quit_game(self):
        self.screen.bye()


class Food:
    pass


class Board():
    def __init__(self, square_size: int = 40):
        self.square_size = square_size
        self.screen = Screen()
        print(self.width(), self.height())

    def width(self):
        return int(self.screen.screensize()[0] / self.square_size)

    def height(self):
        return int(self.screen.screensize()[1] / self.square_size)

    def setup(self, *args, **kwargs):
        self.screen.setup(*args, **kwargs)
        self.draw_border()



    def draw_border(self):
        self.screen.tracer(500)
        tim = Turtle()
        tim.hideturtle()
        tim.color("blue")
        tim.pensize(4)
        tim.penup()
        tim.goto(self.screen.screensize())
        tim.pendown()
        print(self.screen.screensize())
        tim.setheading(270)
        tim.forward(self.screen.screensize()[1] * 2)
        tim.setheading(180)
        tim.forward(self.screen.screensize()[0] * 2)
        tim.setheading(90)
        tim.forward(self.screen.screensize()[1] * 2)
        tim.setheading(0)
        tim.forward(self.screen.screensize()[0] * 2)
        self.update()

    def listen(self):
        self.screen.listen()

    def onkey(self, *args, **kwargs):
        self.screen.onkey(*args, **kwargs)

    def bgcolor(self, *args):
        self.screen.bgcolor(*args)

    def tracer(self, *args):
        self.screen.tracer(*args)

    def update(self, *args):
        self.screen.update(*args)

    def exitonclick(self):
        self.screen.exitonclick()

class ScoreBoard:
    pass


def main():
    the_screen = Board(40)
    the_screen.screen.screensize(640, 640)
    the_screen.setup(width=1.0, height=1.0)
    the_screen.bgcolor("black")
    snake1 = Snake(the_screen)
    the_screen.onkey(key="Left", fun=snake1.turn_left)
    the_screen.onkey(key="Right", fun=snake1.turn_right)
    the_screen.onkey(key="q", fun=snake1.quit_game)
    the_screen.onkey(key="r", fun=snake1.reset)
    the_screen.listen()
    while True:
        snake1.move()
        snake1.wall_collision_detect()
#       snake1.self_collision_detect()
        snake1.food_collision_detect()
        sleep(0.125)
    the_screen.exitonclick()


if __name__ == "__main__":
    main()
