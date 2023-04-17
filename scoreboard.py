from turtle import Turtle, Screen
screen = Screen()
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.score = 0
        self.penup()
        self.goto(0, 280)
        self.update_score()
        self.response = []

    def update_score(self):
        self.write(f"Score: {self.score}", align='center', font=("Courier", 15, "normal"))

    def increase_score(self):
        self.clear()
        self.score += 1
        self.update_score()

    def new_game(self):
        self.response = screen.textinput(title="PLAY AGAIN?", prompt="Type Yes or No")

    def new_score(self):
        self.clear()
        self.score *= 0
        self.update_score()

    def end_game(self):
        self.goto(0, 0)
        self.write(f"Game over!!!, Your Score: {self.score},", align='center', font=("Courier", 15, "normal"))
