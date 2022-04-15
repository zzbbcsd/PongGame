from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height = 600)
screen.bgcolor('black')
screen.title("Welcome to Abby's PingPong game")
screen.tracer(0)

paddle_r = Paddle((350,0))
paddle_l = Paddle((-350,0))

ball = Ball()

score = Scoreboard()

screen.listen()
screen.onkey(paddle_r.up, 'Up')
screen.onkey(paddle_r.down, 'Down')
screen.onkey(paddle_l.up, 'w')
screen.onkey(paddle_l.down, 's')


game_on = True

while game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # detect collision

    if ball.ycor() > 280 or ball.ycor() < -280:
        #bounce
        ball.bounce_y()

    # detect collision with paddle
    if ball.distance(paddle_r) < 50 and ball.xcor() > 320:
        ball.bounce_x()

    if ball.distance(paddle_l) < 50 and ball.xcor() < -320:
        ball.bounce_x()


    # detect when paddle missed the ball
    if ball.xcor() > 380:
        ball.goback()
        # left player gets a point
        score.got_point_l()

    if ball.xcor() < -380:
        ball.goback()

        score.got_point_r()

screen.exitonclick()