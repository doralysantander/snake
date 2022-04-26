from turtle import Screen, Turtle
import time 

#crear un objeto del escenario
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Programate snake")

#desactive la animacion
screen.tracer(0)

#creacion cuerpo de la serpiente

starting_positions = [(0,0),(-20,0),(-40,0)]

segments =[]

for position in starting_positions:
    snake_segment = Turtle("square")# creo objeto serpiente
    snake_segment.color("white")
    snake_segment.penup()# quitar la linea
    snake_segment.goto(position)#cordenadas x,y  en y =0
    segments.append(snake_segment)#agregar un elemento a lista

#estado juego
game_is_on = True

while game_is_on:
    screen.update()
    #aumentar velocidad
    time.sleep(0.2)

    '''
    for segment in segments:
        segment.forward(20)# cada segmento se vaya 20 esp
        segment[0].left(90)    

    '''

    for seg_num in range(len(segments) -1, 0, -1 ):
        new_x = segments[seg_num -1].xcor()
        new_y = segments[seg_num -1].ycor()
        segments[seg_num].goto(new_x, new_y)


    segments[0].forward(20)
    segments[0].left(90) 


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

