from turtle import Turtle, Screen

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.lscore = 0
        self.rscore = 1
        self.goto(-180, 280)
        self.write(self.lscore, align = 'center', font("Courier 80 nr"))