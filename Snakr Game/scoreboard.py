from turtle import Turtle



class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt", mode="r") as data1:
            self.highscore=int(data1.read())
        self.color("white")
        self.penup()
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(-100,317)
        self.write(arg=f"Score {self.score}", align="center", font=("Courier", 24, "normal"))
        self.goto(150, 317)
        self.write(arg=f"High Sore :{self.highscore}", align="center", font=("Courier", 24, "normal"))

    def reset_highscore(self):
        if self.highscore < self.score:
            self.highscore = self.score
            with open("data.txt", mode="w") as data2:
                data2.write(f"{self.highscore}")
        self.score = 0
        self.update_score()

    def increase_score(self):
     self.score+=1
     self.clear()
     self.update_score()
