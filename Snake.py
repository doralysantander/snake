from turtle import Screen, Turtle

#crear un objeto del escenario
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Programate snake")

#creacion cuerpo de la serpiente

positions = [(0,0),(-20,0),(-40,0)]

for position in positions:
    snake_segment = Turtle("square")# creo objeto serpiente
    snake_segment.color("white")
    snake_segment.goto(position)#cordenadas x,y  en y =0
'''
snake_segment = Turtle("square")# creo objeto serpiente
snake_segment.color("white")

snake_segment2 = Turtle("square")# creo objeto serpiente
snake_segment2.color("white")
snake_segment2.goto(-20,0)#cordenadas x,y  en y =0

snake_segment3 = Turtle("square")# creo objeto serpiente
snake_segment3.color("white")
snake_segment3.goto(-40,0)'''

#final
screen.exitonclick()

