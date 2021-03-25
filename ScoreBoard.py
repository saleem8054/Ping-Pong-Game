from turtle import Turtle
class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()
        
    def update_scoreboard(self):
        self.clear()
        self.goto(-100,230)
        self.write(self.l_score,align="center",font=("Courier", 50, "bold"))
        self.goto(100,230)
        self.write(self.r_score,align="center",font=("Courier", 50, "bold"))

                
    def update_score_l(self):
        self.l_score += 1
        self.update_scoreboard()
        
    def update_score_r(self):
        self.r_score += 1
        self.update_scoreboard()
        
