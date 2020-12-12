"""OOP version of Snake Game"""
##################################################
# Imports and type definitions
from time import sleep
from snake import Snake, Board, Food


def main():
    the_screen = Board(40)
    the_screen.screen.screensize(380, 380)
    the_screen.setup(width=1.0, height=1.0)
    the_screen.bgcolor("black")
    snake1 = Snake(the_screen)
    the_screen.onkey(key="Left", fun=snake1.turn_left)
    the_screen.onkey(key="Right", fun=snake1.turn_right)
    the_screen.onkey(key="q", fun=snake1.quit_game)
    the_screen.onkey(key="r", fun=snake1.reset)
    the_screen.listen()
    my_food = Food(the_screen)
    my_food.place_food()
    while True:
        snake1.move()
#        snake1.wall_collision_detect()
#       snake1.self_collision_detect()
        if snake1.food_collision_detect(my_food):
            my_food.eat()
            my_food = Food(the_screen)
            my_food.place_food()
        sleep(0.125)
    the_screen.exitonclick()


if __name__ == "__main__":
    main()
