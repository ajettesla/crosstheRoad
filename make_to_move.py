from turtle import Turtle


class make_player:
    def __init__(self):
        global timmy

    def make_turtle(self):
        timmy = Turtle(shape="turtle")
        timmy.color("red")
        timmy.shapesize(stretch_len=1, stretch_wid=1)
        timmy.penup()
        timmy.goto(0, -370)

    def move_up(self):
        timmy.setheading(90)
        timmy.forward(10)
