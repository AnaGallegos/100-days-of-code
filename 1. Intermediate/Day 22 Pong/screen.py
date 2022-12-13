from turtle import Screen
from paddles import Paddle
from scoreboard import Scoreboard
from ball import Ball
import time

screen = Screen()

screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

rpaddle = Paddle((350,0))
lpaddle = Paddle((-350,0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()

screen.onkey(rpaddle.go_up, 'Up')
screen.onkey(rpaddle.go_down, 'Down')

screen.onkey(lpaddle.go_up, 'w')
screen.onkey(lpaddle.go_down, 's')

print(rpaddle.ycor())


game_on = True
x = 0.1
while game_on:
    time.sleep(x)
    screen.update()
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    if ball.distance(rpaddle) < 50 and ball.xcor() > 325 or ball.distance(lpaddle) < 50 and ball.xcor() < -325:
        ball.bounce_x()

    if ball.xcor() > 400 :
        ball.reset()
        scoreboard.l_point()
        x *= 0.8        

    if ball.xcor() < -400:
        ball.reset()
        scoreboard.r_point()
        x *= 0.8


screen.exitonclick()