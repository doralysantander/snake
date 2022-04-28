from turtle import  Turtle

#creacion cuerpo de la serpiente
STARTING_POSITIONS = [(0,0),(-20,0),(-40,0)]
DOWN = 270
UP = 90
RIGHT = 0
LEFT = 180


class Snake:

        def __init__(self):
            self.segments = []#atributo
            self.create_snake()#metodo crear serpiente
            self.head = self.segments[0]#almacena la cabeza

        def create_snake(self):
            for position in STARTING_POSITIONS:
                self.add_segment(position)
                
        def add_segment(self,position):
                snake_segment = Turtle("square")# creo objeto serpiente
                snake_segment.color("white")
                snake_segment.penup()# quitar la linea
                snake_segment.goto(position)#cordenadas x,y  en y =0
                self.segments.append(snake_segment)#agregar un 

        #extienda la serpiente
        def extend(self):
            self.add_segment(self.segments[-1].position())
            
        def move(self):
            #movimiento de la serpiente
            for seg_num in range(len(self.segments) -1, 0, -1 ):
                new_x = self.segments[seg_num -1].xcor()
                new_y = self.segments[seg_num -1].ycor()
                self.segments[seg_num].goto(new_x, new_y)


            self.head.forward(20)
            #segments[0].left(90)

        def up(self):
            if self.head.heading() != DOWN:
                self.head.setheading(UP)

        def down(self):
            if self.head.heading() != UP:
                self.head.setheading(DOWN)

        def left (self):
            if self.head.heading() != RIGHT:
                self.head.setheading(LEFT) 

        def right(self):
            if self.head.heading() != LEFT:
                self.head.setheading(RIGHT)

        '''
        snake_segment = Turtle("square")# creo objeto serpiente
        snake_segment.color("white")

        snake_segment2 = Turtle("square")# creo objeto serpiente
        snake_segment2.color("white")
        snake_segment2.goto(-20,0)#cordenadas x,y  en y =0

        snake_segment3 = Turtle("square")# creo objeto serpiente
        snake_segment3.color("white")
        snake_segment3.goto(-40,0)'''



