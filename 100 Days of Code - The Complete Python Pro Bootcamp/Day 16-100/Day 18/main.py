import turtle
from turtle import Turtle,Screen
import random

eve=Turtle("turtle")
eve.color("red", "green")
# eve.pensize(15)
# eve.penup()
# eve.sety(-200)
# eve.pendown()
# def square():
#
#     eve.forward(100)
#     eve.left(90)
#     eve.forward(100)
#     eve.left(90)
#     eve.forward(100)
#     eve.left(90)
#     eve.forward(100)
# square()
#
#
# def dash_line():
#     eve.forward(10)
#     eve.penup()
#     eve.forward(5)
#     eve.pendown()
#
# for i in range(20):
#     dash_line()

'''Drawing different shapes below'''
#
# def triangle():
#     eve.color("green")
#     eve.forward(100)
#     eve.left(135)
#     eve.forward(100)
#     eve.left(90)
#     eve.forward(100)
#     eve.left(135)
#     eve.forward(50)
#
#
# def square():
#     eve.color("blue")
#     eve.forward(100)
#     eve.left(90)
#     eve.forward(100)
#     eve.left(90)
#     eve.forward(150)
#     eve.left(90)
#     eve.forward(100)
#     eve.left(90)
#
#
# def pentagon():
#     eve.color("grey")
#     eve.forward(150)
#     eve.left(72)
#     eve.forward(150)
#     eve.left(72)
#     eve.forward(150)
#     eve.left(72)
#     eve.forward(150)
#     eve.left(72)
#     eve.forward(150)
#     eve.left(72)
#
# def hexagon():
#     eve.color("pink")
#     eve.forward(150)
#     eve.left(60)
#     eve.forward(150)
#     eve.left(60)
#     eve.forward(150)
#     eve.left(60)
#     eve.forward(150)
#     eve.left(60)
#     eve.forward(150)
#     eve.left(60)
#     eve.forward(150)
#     eve.left(60)
#
# def heptagon():
#     eve.color("yellow")
#     eve.forward(150)
#     eve.left(51.4285)
#     eve.forward(150)
#     eve.left(51.4285)
#     eve.forward(150)
#     eve.left(51.4285)
#     eve.forward(150)
#     eve.left(51.4285)
#     eve.forward(150)
#     eve.left(51.4285)
#     eve.forward(150)
#     eve.left(51.4285)
#     eve.forward(150)
#     eve.left(51.4285)
#
# def octagon():
#     eve.color("maroon")
#     eve.forward(150)
#     eve.left(45)
#     eve.forward(150)
#     eve.left(45)
#     eve.forward(150)
#     eve.left(45)
#     eve.forward(150)
#     eve.left(45)
#     eve.forward(150)
#     eve.left(45)
#     eve.forward(150)
#     eve.left(45)
#     eve.forward(150)
#     eve.left(45)
#     eve.forward(150)
#     eve.left(45)
#
# def nonagon():
#     eve.color("orange")
#     eve.forward(150)
#     eve.left(40)
#     eve.forward(150)
#     eve.left(40)
#     eve.forward(150)
#     eve.left(40)
#     eve.forward(150)
#     eve.left(40)
#     eve.forward(150)
#     eve.left(40)
#     eve.forward(150)
#     eve.left(40)
#     eve.forward(150)
#     eve.left(40)
#     eve.forward(150)
#     eve.left(40)
#     eve.forward(150)
#     eve.left(40)
#
# def decagon():
#     eve.color("black")
#     eve.forward(150)
#     eve.left(36)
#     eve.forward(150)
#     eve.left(36)
#     eve.forward(150)
#     eve.left(36)
#     eve.forward(150)
#     eve.left(36)
#     eve.forward(150)
#     eve.left(36)
#     eve.forward(150)
#     eve.left(36)
#     eve.forward(150)
#     eve.left(36)
#     eve.forward(150)
#     eve.left(36)
#     eve.forward(150)
#     eve.left(36)
#     eve.forward(150)
#     eve.left(36)
#
# def all_shapes():
#     triangle()
#     square()
#     pentagon()
#     hexagon()
#     heptagon()
#     octagon()
#     nonagon()
#     decagon()
#
# all_shapes()
# colours=["medium violet red","pale goldenrod","olive","light sky blue","gainsboro","tomato","medium sea green"]
# def draw_shape(num_sides):
#     angle=360/num_sides
#     for i in range(num_sides):
#         eve.forward(100)
#         eve.right(angle)
# for sides_of_shape in range(3,11):
#     eve.color(random.choice(colours))
#     draw_shape(sides_of_shape)

'''Random walk'''

# directions=[0,90,180,270]
# for _ in range(200):
#     eve.color(random.choice(colours))
#     eve.forward(30)
#     eve.setheading(random.choice(directions))



'''Generating random RGB colors'''
turtle.colormode(255)
def random_color():
    r=random.randint(0,255)
    g=random.randint(0,255)
    b =random.randint(0, 255)
    random_color=(r,g,b)
    return random_color
eve.speed("fastest")

def spirograph(gap_size):
    for _ in range(int(360/gap_size)):
        eve.color(random_color())
        eve.circle(100)
        eve.setheading(eve.heading()+gap_size)



spirograph(2)



screen=Screen()
screen.exitonclick()