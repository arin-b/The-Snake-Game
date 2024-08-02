from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.goto(-10, 280)
        self.color("white")
        self.hideturtle()

    def display_score(self, score):
        self.clear()
        self.write(arg=f"Score: {score}", align="center", font=("Courier", 14, "normal"))

    def end_game(self, score):
        self.goto(0, -10)
        self.clear()
        self.write(arg=f"Game Over\nYour score is: {score}", align="center", font=("Courier", 18, "normal"))