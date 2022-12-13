import turtle as tur
from turtle import Turtle, Screen
import random

def change_color():
    R = random.random()
    B = random.random()
    G = random.random()

    timmy.color(R, G, B)

timmy = tur.Turtle()
timmy.shape('turtle')
timmy.color('gold')



# colors = ['yellow', 'gold', 'orange', 'red', 'maroon', 'violet', 'magenta', 'purple', 'navy', 'blue', 'lightgreen', 'green', 'darkgreen']

# timmy.speed('fastest')
# for i in range(15):
#     for color in ('red', 'magenta', 'blue',
#                   'cyan', 'green', 'white',
#                   'yellow'):
#         timmy.color(color)
#         timmy.circle(100)
#         timmy.left(5)
     

# direc = [0, 90, 180, 270]
# timmy.pensize(10)
# timmy.speed('fastest')
# for i in range(200):
#     # timmy.color(random.choice(colors))
#     change_color()
#     timmy.forward(15)
#     choice = random.choice(direc)
#     timmy.left(int(choice))
       

# lados = 3
# for i in range(3,11):
#     timmy.color(random.choice(colors))
#     for l in range(lados):
#         timmy.forward(100)
#         timmy.left(float(360/lados))
#     lados += 1    









screen = Screen()
screen.exitonclick()
