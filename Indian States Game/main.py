import pandas
from turtle import Turtle,Screen
score = 0
guessed_list = []
data = pandas.read_csv("28_states_india.csv")
data_state = data.states

screen =Screen()
tim =Turtle()
screen.setup(height=800,width=800)
screen.bgpic("indian political map.gif")

def write(choice):
    new_x = data[data_state==f"{choice}"].x
    new_y = data[data_state==f"{choice}"].y
    tim.penup()
    tim.hideturtle()
    tim.goto(new_x.item(),new_y.item())
    tim.write(f"{choice}")

while score <28:
    guess = screen.textinput(f"{score}/28 Guess a state","Do you know any state name ?").title()
    if guess == "Exit":
        print(f"You scored {score} out of 28")
        break
    for ele in data_state:
        if ele == guess and guess not in guessed_list:
            score +=1
            guessed_list.append(guess)
            write(guess)



screen.exitonclick()

