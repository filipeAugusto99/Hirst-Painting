# import colorgram

# colors = colorgram.extract("hirst_spot.jpg", 30)

# rgb_colors = []

# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)

from turtle import *
import random

colormode(255)

colors_list = [
    (241, 119, 38),
    (240, 77, 93),
    (163, 111, 8),
    (131, 215, 207),
    (239, 96, 29),
    (167, 45, 137),
    (28, 35, 41),
    (85, 183, 6),
    (53, 93, 86),
    (148, 185, 222),
    (134, 216, 221),
    (249, 207, 0),
    (201, 134, 13),
    (247, 210, 40),
    (133, 197, 171),
    (158, 192, 229),
    (233, 165, 177),
    (43, 77, 72),
    (88, 94, 98),
    (240, 171, 156),
    (27, 39, 37),
    (145, 28, 113),
    (119, 97, 0),
    (116, 136, 137),
]

t = Turtle()
t.color("blue")
t.penup()


y = -250

for _ in range(10):
    y += 50
    x = -220

    for _ in range(10):
        t.setpos(x, y)
        t.dot(20, random.choice(colors_list))
        x += 50

t.home()


sc = Screen()
sc.exitonclick()
