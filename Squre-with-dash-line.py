from turtle import Turtle,Screen
import heroes
import random as r
tim= Turtle()

tim.color("blue")  
for _ in range(4):
 tim.right(90)
 for _ in range(14):
        tim.forward(10)
        tim.penup()
        tim.forward(10)
        tim.pendown()

screen= Screen()
screen.exitonclick()