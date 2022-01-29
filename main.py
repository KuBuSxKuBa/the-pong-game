from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time
s = Screen()
s.setup(width=800 , height=600)
s.bgcolor("black")
s.title("The pong game")
s.tracer(0)

ball = Ball()
scoreboard = Scoreboard()


r_paddle = Paddle((350 , 0))
l_paddle = Paddle((-350 , 0))

s.listen()
s.onkey(r_paddle.go_up ,"Up")
s.onkey(r_paddle.go_down ,"Down")
s.onkey(l_paddle.go_up ,"w")
s.onkey(l_paddle.go_down ,"s")


game_is_on = True
time_amount = 0.1
while game_is_on:
    time.sleep(time_amount)
    ball.move()
    s.update()
    print(time_amount)

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        time_amount -= 0.02
        ball.bounce_x()

    if ball.xcor() > 380:
        time_amount = 0.1
        ball.l_scores()
        scoreboard.l_point()

    if ball.xcor() < -380:
        time_amount = 0.1
        ball.r_scores()
        scoreboard.r_point()
s.exitonclick()