from turtle import Screen
from player import Player
from time import sleep
from home import Home
from traffic import Car

##################################################
# Setup
screen = Screen()
screen.screensize(canvheight=800, canvwidth=800)
my_player = Player(screen=screen)
screen.onkey(key='h', fun=my_player.go_left)
screen.onkey(key='j', fun=my_player.go_down)
screen.onkey(key='k', fun=my_player.go_up)
screen.onkey(key='l', fun=my_player.go_right)
screen.onkey(key='q', fun=exit)
homes = [None] * 6
homes[0] = Home(screen, x=-360, y=320)
homes[1] = Home(screen, x=-240, y=320)
homes[2] = Home(screen, x=-120, y=320)
homes[3] = Home(screen, x=360, y=320)
homes[4] = Home(screen, x=240, y=320)
homes[5] = Home(screen, x=120, y=320)
screen.listen()
car1 = Car(screen)
car2 = Car(screen)
car3 = Car(screen)
car4 = Car(screen)
car5 = Car(screen)
car6 = Car(screen)
car7 = Car(screen)
car8 = Car(screen)

while True:
    screen.tracer(0)
    for home in homes:
        if home.collision(my_player):
            my_player.new_player()
    no_vacancy = True
    for home in homes:
        if home.vacancy:
            no_vacancy = False
    if no_vacancy:
        print("You win")
        exit()
    for car in [car1,car2,car3,car4,car5,car6,car7,car8]:
        car.move()
        if car.distance(my_player.pos()) < 30:
            print("Collision car")
            my_player.new_player()
    screen.update()
screen.exitonclick()