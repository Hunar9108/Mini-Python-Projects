from turtle import Turtle

class Line(Turtle):
    def __init__(self):
        super().__init__()
        self.draw_border()


    def draw_border(self):
        self.goto(0, 350)
        self.setheading(270)
        self.color("white")
        self.hideturtle()
        while self.ycor()>-350:
            self.pensize(5)
            self.pendown()
            self.forward(15)
            self.penup()
            self.forward(15)

