from turtle import Turtle, Screen
import random

colors = ["blue","red","green","yellow","orange","purple"]
y_positions =[40,120,200,-40,-120,-200]
is_race = False
screen = Screen()

user_choice = screen.textinput(title = "Make your bet.",prompt = "Which turtle will win the race? Enter a color: ")
screen.setup(width=600,height = 500)
all_turtles = []

for i in range (6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.goto(x=-230,y=y_positions[i])
    new_turtle.color(colors[i])
    all_turtles.append(new_turtle)
if user_choice:
    is_race = True

while is_race:
    for turtle in all_turtles:
        random_distance  = random.randint(0,10)
        turtle.forward(random_distance)
        if turtle.xcor()>250:
            is_race = False
            winning_color = turtle.pencolor()
            if winning_color == user_choice:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else :
                print(f"You've lost.The {winning_color} turtle is the winner! ")

print(user_choice)
screen.exitonclick()