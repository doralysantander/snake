from turtle import  Turtle

#libreria  random que  genera cosas aleatorias
#comida hereda de turtle
class Food(Turtle):#heredad todos los metodos que tiene turtle

    def __init__(self):
        #heredar todo lo que tiene 
        super().__init__()
        self.shape('circle')
        self.penup()#linea
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("green")


