# Importing the random module.
import random
import turtle as t
t.colormode(255)
tim = t.Turtle()
screen = t.Screen()

color_list = [(245, 243, 239), (246, 243, 244), (202, 164, 109), (240, 245, 242), (236, 239, 243), (153, 75, 49), (222, 201, 136), (53, 94, 124), (171, 153, 41), (136, 32, 21), (133, 163, 184), (197, 93, 73), (48, 123, 87), (73, 44, 36), (14, 97, 72), (145, 178, 148), (91, 73, 75), (233, 176, 165), (160, 143, 159), (54, 47, 50), (184, 205, 172), (35, 61, 75), (22, 85, 89), (146, 19, 21), (86, 146, 130), (38, 67, 91), (13, 72, 66), (106, 128, 155), (175, 99, 101), (176, 192, 209)]
tim.penup()
tim.hideturtle()
tim.speed('fastest')
tim.setheading(255)
tim.forward(300)
tim.setheading(0)
numbers_of_dots = 100

def turtle_painting(numbers_of_dots):
    """
    This function creates a list of random dots and colors them

    :param numbers_of_dots: The number of dots you want to draw
    """
    for dot_count in range(1, numbers_of_dots + 1):
        tim.dot(20, random.choice(color_list))
        tim.forward(50)

        if dot_count % 10 == 0:
            tim.setheading(90)
            tim.forward(50)
            tim.setheading(180)
            tim.forward(500)
            tim.setheading(0)

turtle_painting(numbers_of_dots)
screen.exitonclick()
