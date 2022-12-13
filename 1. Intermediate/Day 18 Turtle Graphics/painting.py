# import colorgram

# colors = colorgram.extract('image.png', 30)
# rgb_colors = []
# print(colors)

# for color in colors:
#     r=color.rgb.r
#     g=color.rgb.g
#     b=color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)

# print(rgb_colors)


import turtle as tur
import random
from turtle import Turtle, Screen, color, pensize

color_list = [(190, 19, 46), (244, 233, 65), (218, 67, 106), (197, 76, 33), (108, 182, 209), (13, 143, 89), (197, 176, 16), (19, 124, 173), (13, 167, 213), (209, 152, 95), (238, 232, 3), (26, 42, 76), (36, 43, 110), (78, 175, 96), (181, 45, 65), (216, 68, 49), (217, 129, 152), (124, 185, 122), (237, 161, 180), (8, 62, 39), (147, 209, 221), (7, 90, 52), (5, 86, 109), (164, 30, 28), (158, 212, 185), (236, 171, 163)]

tim = tur.Turtle()

for i in range (10):
    tim.dot(20, random.choice(color_list))
    tim.penup
    tim.forward
    tim.pendown




screen = Screen()
screen.exitonclick()
