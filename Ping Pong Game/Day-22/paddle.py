from turtle import Turtle

class Paddle(Turtle):
    def __init__(self,x,y):
        super().__init__()
        self.penup()
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(x,y)
        self.color("white")

    def up(self):
        new_y = 20 + self.ycor()
        new_x = self.xcor()
        if -250< new_y <250:
            self.goto(new_x, new_y)

    def down(self):
        new_y = self.ycor() - 20
        new_x = self.xcor()
        if -250< new_y <250:
            self.goto(new_x, new_y)