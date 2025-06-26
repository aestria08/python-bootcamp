# import colorgram
#
# rgb_colors=[]
# colors = colorgram.extract('hirst.jpg', 30)
# for color in colors:
#     r=color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color=(r,g,b)
#     rgb_colors.append(new_color)
# print(rgb_colors)
import random
import turtle
from turtle import Turtle,Screen

from PIL.ImageChops import screen

colors=[(198, 159, 116), (70, 92, 129), (147, 85, 53), (218, 210, 116), (138, 160, 191), (178, 160, 38), (184, 146, 164),
        (28, 32, 46), (58, 34, 23), (120, 70, 93), (139, 175, 154), (77, 115, 79), (143, 25, 16), (186, 97, 82),
        (61, 31, 42), (121, 27, 41), (45, 58, 94), (177, 96, 114), (102, 119, 170), (34, 52, 45), (100, 160, 85),
        (214, 175, 192), (216, 181, 173), (160, 209, 191), (67, 86, 23), (219, 206, 8)]

eve=Turtle()
eve.speed("fastest")
turtle.colormode(255)
eve.penup()
eve.hideturtle()
eve.setheading(225)
eve.forward(300)
eve.setheading(0)
num_of_dots=100

for i in range (1,num_of_dots+1):

    eve.dot(20,random.choice(colors))
    # eve.penup()
    eve.forward(50)
    # eve.pendown()

    if i%10==0:
        eve.setheading(90)
        # eve.penup()
        eve.forward(50)
        # eve.pendown()
        eve.setheading(180)
        # eve.penup()
        eve.forward(500)
        # eve.pendown()
        eve.setheading(0)


screen=Screen()
screen.exitonclick()
