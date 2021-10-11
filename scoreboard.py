from turtle import Turtle

ALIGMENT = "center"
FONT = ('Courier', 18, 'normal')


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 260)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}", move=False,
                   align=ALIGMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", move=False,
                   align=ALIGMENT, font=FONT)

    def increase_score(self, by_amount):
        self.score += by_amount
