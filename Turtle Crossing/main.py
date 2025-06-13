import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard


screen = Screen()
screen.setup(width=600, height=600)
screen.listen()
screen.tracer(0)

player = Player()
scoreboard = Scoreboard()
car_manager=CarManager()

#Move the turtle on the screen to cross the road
screen.onkey(player.move , "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    car_manager.create_car()
    car_manager.move_cars()

    # Reached other side of road
    if player.other_side():
        player.next_level()
        scoreboard.level+=1

    # collision with car
    for car in car_manager.cars_list:
        if player.distance(car)<=20:
            game_is_on = False

    scoreboard.tell_level()
    screen.update()

scoreboard.game_over()
screen.exitonclick()
