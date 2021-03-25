from turtle import Turtle
import time
class Ball(Turtle):
    def __init__(self):
        super().__init__("circle")
        self.penup()
        self.color("red")
        self.x_increment = 5
        self.y_increment = 5
    def move(self):
        self.new_x_cor = self.xcor() + self.x_increment
        self.new_y_cor = self.ycor() + self.y_increment        
        
        self.goto(self.new_x_cor,self.new_y_cor)
        
    def bounce_y(self):
        self.y_increment *= -1
        
    def bounce_x(self):
        self.x_increment *= -1
        
    def reset_position(self):   
        self.goto((0,0))
        self.bounce_x()
        