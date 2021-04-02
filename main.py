from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
import time
from scoreboard import ScoreBoard


screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Manny Pong")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")




game_is_on = True
while game_is_on:
    time.sleep(ball.move_faster)
    screen.update()
    ball.move()

    # Detect collision with screen

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320  or ball.distance(l_paddle) < 50 and ball.xcor() > -320:
        ball.bounce_x()


    # Detect when Right paddle misses
    if ball.xcor() > 380:
        scoreboard.increase_l_score()
        scoreboard.update_scoreboard()
        ball.reset_position()

    # Detect when Right paddle misses
    if ball.xcor() < -380:
        scoreboard.increase_r_score()
        scoreboard.update_scoreboard()
        ball.reset_position()

screen.exitonclick()
