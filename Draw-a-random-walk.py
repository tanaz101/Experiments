from turtle import Turtle,Screen
import heroes
import random as r
tim= Turtle()



tim.screen.bgcolor("pink") 
deegre=[90,0,180,270]
tim.pensize(10)
color=["aqua","aquamarine","beige","blue","red","green","seagreen"]

tim.speed("fastest")
for _ in range(200):
        tim.color(r.choice(color))
        tim.forward(30)
        tim.setheading(r.choice(deegre))
screen= Screen()
screen.exitonclick()