# import colorgram
# colors=colorgram.extract("/Users/tanazzafri/python/Experiments/img/hirst.jpg",140)
# rgb_list=[]
# for color in colors:
#     r=color.rgb.r
#     g=color.rgb.g
#     b=color.rgb.b
#     tuple_rgb=(r,g,b)
#     rgb_list.append(tuple_rgb)
# print(rgb_list)

import turtle as t
import random as r
screen=t.Screen()
screen.title("The Hirst Painting Project")
t.colormode(255)
color_list=[(248, 232, 236), (232, 142, 77), (230, 65, 102), (246, 220, 81), (7, 175, 214), (210, 232, 238), (161, 53, 106), (233, 77, 60), (2, 132, 168), (86, 186, 211), (232, 125, 156), (143, 211, 221), (154, 77, 55), (41, 168, 106), (117, 191, 152), (1, 153, 92), (174, 147, 60), (240, 156, 177), (179, 199, 194), (27, 84, 62), (75, 53, 85), (20, 61, 122), (36, 65, 86), (75, 67, 48), (0, 109, 114), (245, 166, 153), (101, 125, 163), (175, 190, 213)]

tim=t.Turtle()
tim.speed("fastest")
tim.penup()
tim.hideturtle()
tim.setheading(225)
tim.forward(350)
tim.setheading(360)
num=110
for dor_count in range(1,num+1):
    tim.dot(20,r.choice(color_list))
    tim.forward(50)
    if dor_count%10==0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(360)


screen.exitonclick()