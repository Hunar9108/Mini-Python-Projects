from turtle import Turtle
COORDINATES = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20

class Snake :
    def __init__(self):
        self.segments  = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in COORDINATES:
            self.add_segment(position)

    def reset_snake(self):
        for seg in self.segments:
            seg.goto(900,900)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]


    def add_segment(self,position):
        tim = Turtle("square")
        tim.color("white")
        tim.penup()
        tim.goto(position)
        self.segments.append(tim)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        for i in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[i - 1].xcor()
            new_y = self.segments[i - 1].ycor()
            self.segments[i].goto(new_x, new_y)
        self.segments[0].forward(MOVE_DISTANCE)

    def up(self):
        self.head.setheading(90)
    def down(self):
        self.head.setheading(270)
    def right(self):
        self.head.setheading(0)
    def left(self):
        self.head.setheading(180)