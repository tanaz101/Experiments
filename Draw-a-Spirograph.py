from turtle import Turtle,Screen
import heroes
import random as r
tim= Turtle()


color=["aqua","aquamarine","beige","blue","red","green","seagreen"]

tim.speed("fastest")
def draw(size):
 for i in range(int(360/size)):      
    tim.color(r.choice(color)) 
    current_heading=tim.heading()
    tim.setheading(current_heading+size)
    tim.circle(100)
draw(5)



screen= Screen()
screen.exitonclick()