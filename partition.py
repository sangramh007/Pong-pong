from turtle import Turtle


class Partition(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.width(5)
        self.penup()
        self.hideturtle()
        self.goto(0, 300)
        self.setheading(270)

    def create_partition(self):
        while self.ycor() != -280:
            self.forward(10)
            self.pendown()
            self.forward(10)
            self.penup()
