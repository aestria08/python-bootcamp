import turtle
from turtle import Turtle,Screen

tim=Turtle()
screen=Screen()
'''Using keyboards'''
turtle.listen()

def move_forwards():
    tim.forward(100)
turtle.onkey(key='w',fun=move_forwards)

def move_backwards():
    tim.backward(100)
turtle.onkey(key='s',fun=move_backwards)

def move_left():
    tim.left(10)
turtle.onkey(key='a', fun=move_left)

def move_right():
    new=tim.heading()+10
    tim.setheading(new)
turtle.onkey(key='d', fun=move_right)

def clear_screen():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()
turtle.onkey(key='c',fun=clear_screen)

screen.exitonclick()