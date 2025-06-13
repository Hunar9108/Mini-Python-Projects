import time
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
from  line import Line

screen = Screen()
screen.bgcolor("black")
screen.setup(height=600,width=800)
screen.title("Pong Game")
screen.tracer(0)

line = Line()
pad_r = Paddle(350,0)
pad_l=Paddle(-350,0)
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(pad_r.up,"Up")
screen.onkeypress(pad_r.down,"Down")
screen.onkeypress(pad_l.up,"w")
screen.onkeypress(pad_l.down,"s")


game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    if ball.ycor()>280 or -280>ball.ycor():
        ball.bounce()

    if ball.distance(pad_r)<50 and ball.xcor()>320or ball.distance(pad_l)<50 and ball.xcor()<-320:
        ball.hit()


    if ball.xcor()>380 :
        ball.reset_ball()
        scoreboard.l_point()

    if ball.xcor()<-380:
        ball.reset_ball()
        scoreboard.r_point()


screen.exitonclick()
