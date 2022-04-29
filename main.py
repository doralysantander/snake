from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard

import time 


#crear un objeto del escenario
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Programate snake")

#desactive la animacion
screen.tracer(0)

#instaciar el objeto cerpiente
snake = Snake()

#crear instancia Eel objeto comida
food= Food()

#CREAR OBJETO TABLERO PUNTOS
scoreboard= Scoreboard()

#movimientos serpiente
screen.listen()
screen.onkey(snake.up,"Up")#teclas
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

#estado juego
game_is_on = True

while game_is_on:
    screen.update()
    #aumentar velocidad
    time.sleep(0.2)
    snake.move()  

    #detectar colision con comida 
    if snake.head.distance(food) < 15:
        food.refresh() 
        scoreboard.increase_score()
        snake.extend()  

    #DETECTAR LAS PAREDES 
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False 
        scoreboard.game_over()   

    #detectar colision cola   
    for segment in snake.segments:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:#-1
            for segment in snake.segments[1:]: 
                if snake.head.distance(segment) < 10:       
                    game_is_on = False 
                    scoreboard.game_over()




#final
screen.exitonclick()












'''for segment in snake.segments:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
    for segment in snake.segments[-1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()'''