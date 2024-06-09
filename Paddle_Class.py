from turtle import *

class Paddle(Turtle):
    def __init__(self,x_axis):
        super().__init__()
        self.shape("square")
        self.penup()
        self.color("white")
        self.goto((x_axis,0))
        self.shapesize(5,1,0)
        
    def mov_up(self):
        xaxis=self.xcor()
        yaxis=self.ycor()
        self.goto((xaxis,yaxis+20))
    def mov_down(self):
        xaxis=self.xcor()
        yaxis=self.ycor()
        self.goto((xaxis,yaxis-20))
        


