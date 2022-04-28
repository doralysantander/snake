from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0 #atributo
        self.goto(0,270)
        self.color("white")
        self.update_score()#llama a la funcion
        self.hideturtle() # oculta el triangulo


    def update_score(self):

        self.write(f"El puntaje es: {self.score}",font=("Arial",24,"normal"), align="center")   

#funcion sume
    def increase_score(self):
        #limpie lo que habia
        self.clear()
        self.score += 1 
        self.update_score()