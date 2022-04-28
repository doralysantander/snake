from turtle import  Turtle

#libreria  random que  genera cosas aleatorias
import random

#comida hereda de turtle
class Food(Turtle):#heredad todos los metodos que tiene turtle

    def __init__(self):
        #heredar todo lo que tiene Turle 
        super().__init__()
        self.shape('circle')
        self.penup()#linea
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("green")
        self.refresh()# cada ves se refresque

    #aparezca la comida distos lugares
    def refresh(self):
        random_x  = random.randint(-200, 200)#genera un numero entero -200 a 200
        random_y = random.randint(-200, 200)
        self.goto(random_x,random_y)
