from turtle import *
import random

screen = Screen()
screen.setup(500,400)
race_on = False
all_turtles = []

user_bet = screen.textinput('Make your bet', 'Wich turtle will win the race? Enter a color')
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple', 'pink']
y_positions = [-70, -40, -10, 20, 50, 80, 110]
for turtle_index in range(0,7):
    new_turtle = Turtle('turtle')
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(x= -220, y= y_positions[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    race_on = True

while race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 200:
            turtle.speed(7)
            turtle.right(360*3)
            winning_color = turtle.pencolor()
            race_on = False
            if winning_color == user_bet:
                print(f'You won, the {winning_color} turtle is the winner!!')
                
            else:
                print(f'You lose, the {winning_color} turtle is the winner :(')
                turtle.write("YOU LOSE", True, align="center")
        random_distance = random.randint(0,20)
        turtle.forward(random_distance)
screen.exitonclick()
