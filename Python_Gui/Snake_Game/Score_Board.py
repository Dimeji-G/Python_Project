from turtle import Turtle

FONT =  ("Arial 22 normal")

class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        try:
            with open("data.txt") as data:
                self.high_score = int(data.read())
        except:
            self.high_score = 0
        self.color("white")
        self.penup()
        self.goto(0,220)
        self.hideturtle()
        self.update_scoreboard()
        
    
    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}\t High Score: {self.high_score}", align = "center",
                   font = FONT)
        
    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="a") as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.update_scoreboard()


    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align = "center", font = FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()
