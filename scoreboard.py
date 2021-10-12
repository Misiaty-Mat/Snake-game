from turtle import Turtle

ALIGMENT = "center"
FONT = ('Courier', 18, 'normal')


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0

        with open("data.txt") as data:
            record = data.read()
            if record == '':
                self.high_score = 0
            else:
                self.high_score = int(record)

        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 260)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", move=False,
                   align=ALIGMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", "w") as data:
                data.write(str(self.score))

        self.score = 0
        self.update_scoreboard()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER", move=False,
    #                align=ALIGMENT, font=FONT)

    def increase_score(self, by_amount):
        self.score += by_amount
