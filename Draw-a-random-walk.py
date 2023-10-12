from turtle import Turtle,Screen
import heroes
import random as r
tim= Turtle()
screen= Screen()
screen.title("Random Walk")


tim.screen.bgcolor("pink") 
deegre=[90,0,180,270]
tim.pensize(10)
color=["aqua","aquamarine","beige","blue","red","green","seagreen"]
tim.speed("fastest")
tim.penup()
tim.setheading(225)
tim.forward(180)

for _ in range(200):
        tim.pendown()
        tim.color(r.choice(color))
        tim.forward(30)
        tim.setheading(r.choice(deegre))

screen.exitonclick()