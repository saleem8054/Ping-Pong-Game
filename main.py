from ScoreBoard import ScoreBoard
from Ball import Ball
from paddle import Paddle
from turtle import Turtle,Screen
import time

PADDLE_INITIAL_POSITION_RIGHT = (430,0)
PADDLE_INITIAL_POSITION_LEFT = (-440,0)


screen = Screen()
screen.setup(900,600)
screen.bgcolor("black")
screen.title("Arcade Game")
screen.listen()
screen.tracer(0)

paddle1 = Paddle(PADDLE_INITIAL_POSITION_LEFT)
paddle2 = Paddle(PADDLE_INITIAL_POSITION_RIGHT)
ball = Ball()
scoreBoard = ScoreBoard()


screen.onkeypress(paddle2.up, "Up")
screen.onkeypress(paddle2.down, "Down")


screen.onkeypress(paddle1.up, "w")
screen.onkeypress(paddle1.down, "s")

game_is_on = True

while game_is_on:
    screen.update()
    ball.move()
    
    if ball.ycor() > 280 or ball.ycor() < -280 :
        ball.bounce_y()
        
    if ball.xcor() > 445:
        ball.reset_position()
        scoreBoard.update_score_r()
        
    if ball.xcor() < -445:
        ball.reset_position()
        scoreBoard.update_score_l()
    
    if paddle2.distance(ball) < 50 and ball.xcor() > 410 or paddle1.distance(ball) < 50 and ball.xcor() < -410 :
        ball.bounce_x()







screen.exitonclick()