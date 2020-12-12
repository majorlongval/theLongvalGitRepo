from turtle import _Screen

TABLE_HEIGHT = 600
TABLE_WIDTH = 800


class Table(_Screen):

    def __init__(self):
        super().__init__()


table = Table()
table.bgcolor("black")
table.setup(TABLE_WIDTH, TABLE_HEIGHT)
