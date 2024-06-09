from turtle import Turtle

class Scorecard(Turtle):
    score=0
    def __init__(self,position):
        super().__init__()
        self.score=0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.shapesize(20)
        self.goto(position)
        self.write(f"Score {self.score}",True,font=('Arial', 20, 'normal'))

    def increase_score(self,position):
        self.clear()
        self.score=self.score+1
        self.color("white")
        self.penup()
        self.hideturtle()
        self.shapesize(20)
        self.goto(position)
        self.write(f"Score {self.score}",True,font=('Arial', 20, 'normal'))

        

    


