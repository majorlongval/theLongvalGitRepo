##################################################
# Imports and type definitions
from turtle import Turtle
from turtle import Screen
from random import randint
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
        self.wall_collision_detect()

    def delete_segment(self, segment: int = 0):
        self[segment].hideturtle()
        self.pop(segment)

    def wall_collision_detect(self):
        x_width = self.screen.screen.screensize()[0]
        y_width = self.screen.screen.screensize()[1]
        if (x_width <= self[-1].pos()[0]) or (self[-1].pos()[0] <= (-1 * x_width)):
            print("Collision on left or right")
            self.reset()
        if (y_width <= self[-1].pos()[1]) or (self[-1].pos()[1] <= (-1 * y_width)):
            print("Collision on top or bottom")
            self.reset()

    def self_collision_detect(self):
        position_list = [segment.position() for segment in self]
        int_position_list = [(int(x[0]), int(x[1])) for x in position_list]
        if len(int_position_list) > len(set(int_position_list)):
            print("collision with self")
            self.reset()

    def food_collision_detect(self, the_food):
        if self[-1].pos()[0] == the_food.x and self[-1].pos()[1] == the_food.y:
            print("Food eaten")
            return True
        else:
            return False


    def quit_game(self):
        self.screen.bye()


class Food():
    turtle: Turtle
    x: float
    y: float

    def __init__(self, screen: Screen, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.screen = screen

    def place_food(self):
        self.turtle = Turtle()
        self.turtle.hideturtle()
        self.turtle.penup()
        self.turtle.color('blue')
        self.turtle.shape("square")
        x_maximum = self.screen.screen.screensize()[0]
        y_maximum = self.screen.screen.screensize()[1]
        int_x_on_grid = x_maximum / 20
        int_y_on_grid = y_maximum / 20
        x_pos = randint(-int_x_on_grid, int_x_on_grid) * 20
        y_pos = randint(-int_y_on_grid, int_y_on_grid) * 20
        print("food coord: ", x_pos, y_pos)
        self.turtle.goto(x_pos, y_pos)
        self.x = x_pos
        self.y = y_pos
        self.turtle.showturtle()

    def eat(self):
        self.turtle.hideturtle()
        del self


class Board:
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

    def update(self):
        self.screen.update()

    def exitonclick(self):
        self.screen.exitonclick()


class ScoreBoard:
    pass
