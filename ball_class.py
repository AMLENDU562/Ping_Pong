from turtle import *
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("white")
        self.goto((0,0))
        self.xmov=10
        self.ymov=10
        self.speed=0.1
    def mov(self):
        x_axis=self.xcor()+self.xmov
        y_axis=self.ycor()+self.ymov
        self.goto((x_axis,y_axis))
    def bounce(self):
        self.ymov*=(-1)
    def bounce_x(self):
        self.xmov*=(-1)
        self.speed*=0.9