import random
from turtle import Turtle,Screen
import random
race_on=False
screen=Screen()
screen.setup(height=400,width=500)


user_guess=screen.textinput(title="Make a bet",prompt="What colored turtle will win a race? Choose a color:")
colors=['red','orange','green','blue','purple','yellow']
y_positions=[-100,-70,-40,-10,20,50]
turtles=[]

for turtle_index in range(6):
    new_turtle=Turtle('turtle')
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_positions[turtle_index])
    turtles.append(new_turtle)

if user_guess:
    race_on=True
while race_on:

    for turtle in turtles:
        if turtle.xcor()>230:
            race_on=False
            winning_color=turtle.pencolor()
            if winning_color==user_guess:
                print(f"You have won! The {winning_color} turtle won the race.")
            else:
                print(f"You have lost! The {winning_color} turtle won the race.")

        random_steps=random.randint(0,20)
        turtle.forward(random_steps)


screen.exitonclick()