from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.level = 1

    def tell_level(self):
        self.goto(-210,220)
        self.clear()
        self.write(arg=f"Level: {self.level}" , align = "center", font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.color("black")
        self.write(arg="Game Over", align="center", font=FONT)