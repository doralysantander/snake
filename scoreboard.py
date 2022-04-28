from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0 #atributo
        self.goto(0,270)
        self.color("white")
