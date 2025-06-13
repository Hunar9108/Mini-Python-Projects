import time
from turtle import Screen
from food import Food
from scoreboard import Scoreboard
from snake import Snake

screen = Screen()
screen.setup(height=700,width=700)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

scoreboard = Scoreboard()
snake = Snake()
food = Food()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

game_is_on = True
while game_is_on:

    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food)<15:
        scoreboard.increase_score()
        food.refresh()
        snake.extend()

    if snake.head.xcor()>330 or snake.head.xcor()<-330 or snake.head.ycor()>330 or snake.head.ycor()<-330:
        scoreboard.reset_highscore()
        snake.reset_snake()

    for segment in snake.segments[1:]:
        if snake.head.distance(segment)<10:
            scoreboard.reset_highscore()

            snake.reset_snake()
screen.exitonclick()
 