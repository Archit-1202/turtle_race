import random
from turtle import Turtle, Screen
import random

is_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race?")
colors = ["violet", "indigo", "blue", "green", "yellow", "orange", "red"]
y_pos = [150, 100, 50, 0, -50, -100, -150]
turtles = []

for i in range (0, 7):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[i])
    new_turtle.pu()
    new_turtle.goto(x=-240, y =y_pos[i])
    turtles.append(new_turtle)


if user_bet:
    is_on = True

while is_on == True:
   for i in turtles:
       if i.xcor() > 240:
           winning_color = i.pencolor()
           is_on = False
           if user_bet == winning_color:
               print(f"You've won! the {winning_color} turtle has won")
           else:
               print(f"You've lost! the {winning_color} turtle has won")

       else:
           next_move = random.randint(0, 10)
           i.fd(next_move)




screen.exitonclick()
