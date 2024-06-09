from turtle import *
from Paddle_Class import Paddle
from ball_class import Ball
import time
from Score_card import Scorecard
paddle1=Paddle(-350)
paddle2=Paddle(350)
ball=Ball()


screen=Screen()
screen.setup(width=800,height=700)
screen.bgcolor("black")
screen.title("Ping Pong")
screen.tracer(0)
game_over=True

screen.listen()

screen.onkey(paddle1.mov_up,"w")
screen.onkey(paddle1.mov_down,"s")

screen.onkey(paddle2.mov_up,"Up")
screen.onkey(paddle2.mov_down,"Down")
game_over=True
score1=Scorecard((-200,320))
score2=Scorecard((200,320))

while game_over:
    screen.update()
    time.sleep(ball.speed)
    if(ball.ycor()>280 or ball.ycor()<(-280)):
        ball.bounce()
    if(ball.distance(paddle2)<50 and ball.xcor()>340):
        ball.bounce_x()

    if(ball.distance(paddle1)<50 and ball.xcor()<-340):
        ball.bounce_x()
        
    if(ball.xcor()>400):
        ball.bounce_x()
        score1.increase_score((-200,320))

    if(ball.xcor()<-400):
        ball.bounce_x()
        score2.increase_score((200,320))
        
    ball.mov()
screen.exitonclick()

