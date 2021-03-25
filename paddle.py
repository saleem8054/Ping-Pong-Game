from turtle import Turtle,Screen
import time

class Paddle(Turtle):
    def __init__(self,position):
        super().__init__("square")
        self.color("white")
        self.shapesize(1,5)
        self.penup()
        self.setheading(90)
        self.goto(position)
        
    def up(self):
        if self.ycor() < 230:
            paddle_y_coordinate = self.ycor()
            self.sety(paddle_y_coordinate+20)

    def down(self):
        #while(self.ycor() > -270):
            #screen.update()
            #time.sleep(0.005)
        if self.ycor() > -230:
            paddle_y_coordinate = self.ycor()
            self.sety(paddle_y_coordinate-20)