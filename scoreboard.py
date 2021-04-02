from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.goto(-200, 250)
        self.write(self.l_score, align="center", font=("Arial", 24, "normal"))
        self.goto(200, 250)
        self.write(self.r_score, align="center", font=("Arial", 24, "normal"))

    def update_scoreboard(self):
        self.goto(-200, 250)
        self.write(self.l_score, align="center", font=("Arial", 24, "normal"))
        self.goto(200, 250)
        self.write(self.r_score, align="center", font=("Arial", 24, "normal"))


    def increase_l_score(self):
        self.l_score += 1
        self.clear()


    def increase_r_score(self):
        self.r_score += 1
        self.clear()


