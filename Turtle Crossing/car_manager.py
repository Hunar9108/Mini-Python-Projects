import random
from turtle import Turtle


COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.speed = STARTING_MOVE_DISTANCE
        self.cars_list=[]

    def create_car(self):
        random_chance = random.randint(1,6)
        if random_chance == 2:
            car = Turtle("square")
            car.penup()
            car.shapesize(stretch_wid=1, stretch_len=2)
            car.color(random.choice(COLORS))
            car.goto(300,random.randint(-250,250))
            self.cars_list.append(car)

    def move_cars(self):
        for car in self.cars_list:
            car.backward(self.speed)

    def increase_speed(self):
        self.speed+=MOVE_INCREMENT

