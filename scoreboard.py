from turtle import Turtle
ALIGN = "center"
FONT= ("Arial",24,"normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0 #atributo
        self.goto(0,270)
        self.color("white")
        self.update_score()#llama a la funcion
        self.hideturtle() # oculta el triangulo


    def update_score(self):

        self.write(f"El puntaje es: {self.score}",font=FONT, align=ALIGN)   

#funcion sume
    def increase_score(self):
        #limpie lo que habia
        self.clear()
        self.score += 1 
        self.update_score()

    #termino juego
    def game_over(self):
        self.goto(0,0)
        self.write("Juego terminado:",font=FONT, align=ALIGN)     