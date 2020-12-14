from turtle import Turtle

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.nb_segments = 3
        self.segment_width = 20
        self.starting_position = (0, 0)
        self.segments = []
        self.initiate_segments()
        self.initiate_segments()
        self.heading = RIGHT
        self.head = self.segments[0]

    def initiate_segments(self):
        for i in range(0, self.nb_segments):
            self.add_segment(-self.segment_width*i)

    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.color('white')
        new_segment.penup()
        new_segment.setx(position)
        self.segments.append(new_segment)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        inv_segments = self.segments[::-1]
        for i, seg in enumerate(inv_segments[:-1]):
            seg.goto(x=inv_segments[i + 1].xcor(), y=inv_segments[i + 1].ycor())
        self.head.forward(self.segment_width)

    def change_heading(self, direction):
        self.head.setheading(direction)
        self.heading = direction

    def up(self):
        if self.heading != DOWN:
            self.change_heading(UP)

    def down(self):
        if self.heading != UP:
            self.change_heading(DOWN)

    def left(self):
        if self.heading != RIGHT:
            self.change_heading(LEFT)

    def right(self):
        if self.heading != LEFT:
            self.change_heading(RIGHT)
