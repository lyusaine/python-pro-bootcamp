from turtle import Turtle, Screen
import random
# https://docs.python.org/3/library/turtle.html
# https://cs111.wellesley.edu/reference/colors

colours = [
    "CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue",
    "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"
]

def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        my_turtle.color(random.choice(colours))
        my_turtle.circle(100)
        my_turtle.setheading(my_turtle.heading() + size_of_gap)

my_turtle = Turtle()
my_turtle.hideturtle()
my_turtle.speed("fastest")
my_turtle.pensize(2)

screen = Screen()

draw_spirograph(5)

screen.exitonclick()