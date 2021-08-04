import time
import turtle
from turtle import Turtle
from random import randint

window=turtle.Screen()
turtle.bgcolor('forestgreen')

turtle.color("white")
turtle.shape("turtle")
turtle.speed(0)
turtle.penup()

turtle.setpos(-150,210)
turtle.write(" 'TURTLE RACE' ",font=('arial',30,'bold'))
turtle.penup()

#design of ground

turtle.setpos(-400,-180)
turtle.color('chocolate')
turtle.begin_fill()
turtle.pendown()

turtle.forward(800)
turtle.right(90)

turtle.forward(200)
turtle.right(90)

turtle.forward(800)
turtle.right(90)

turtle.forward(200)
turtle.right(90)

turtle.end_fill()

#FINISH LINE

stamp_size=18
square_size=12
finish_line=200

turtle.color("black")
turtle.shape("square")
turtle.shapesize(square_size/stamp_size)
turtle.penup()

for i in range(13):
    turtle.setpos(finish_line,(150-(i*square_size*2)))
    turtle.stamp()

for j in range(13):
    turtle.setpos(finish_line+square_size,((150-square_size)-(j*square_size*2)))
    turtle.stamp()
    
turtle.hideturtle()

    
#TURTLE 1
turtle1=Turtle()
turtle1.color('white')
turtle1.shape("turtle")
turtle1.speed(0)
turtle1.penup()
turtle1.goto(-250,-140)
turtle1.pendown()

#TURTLE 2
turtle2=Turtle()
turtle2.color('black')
turtle2.shape("turtle")
turtle2.speed(0)
turtle2.penup()
turtle2.goto(-250,-90)
turtle2.pendown()

#TURTLE 3
turtle3=Turtle()
turtle3.color('blue')
turtle3.shape("turtle")
turtle3.speed(0)
turtle3.penup()
turtle3.goto(-250,-50)
turtle3.pendown()


#TURTLE 4
turtle4=Turtle()
turtle4.color('yellow')
turtle4.shape("turtle")
turtle4.speed(0)
turtle4.penup()
turtle4.goto(-250,0)
turtle4.pendown()


#TURTLE 5
turtle5=Turtle()
turtle5.color('green')
turtle5.shape("turtle")
turtle5.speed(0)
turtle5.penup()
turtle5.goto(-250,40)
turtle5.pendown()


#TURTLE 6
turtle6=Turtle()
turtle6.color('red')
turtle6.shape("turtle")
turtle6.speed(0)
turtle6.penup()
turtle6.goto(-250,80)
turtle6.pendown()


#TURTLE 7
turtle7=Turtle()
turtle7.color('indigo')
turtle7.shape("turtle")
turtle7.speed(0)
turtle7.penup()
turtle7.goto(-250,130)
turtle7.pendown()
time.sleep(1)#pause the game for 1 seconds before starting the race



#move the turtles

for i in range(145):
    turtle1.forward(randint(1,5))
    turtle2.forward(randint(1,5))
    turtle3.forward(randint(1,5))
    turtle4.forward(randint(1,5))
    turtle5.forward(randint(1,5))
    turtle6.forward(randint(1,5))
    turtle7.forward(randint(1,5))
    
turtle.exitonclick()
    
















