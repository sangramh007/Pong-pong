from turtle import Turtle

X_POS = [-440, 430]


class Peddle:

    def __init__(self):
        self.peddles = []
        self.create_peddles()

    def create_peddles(self):

        for pos in X_POS:
            peddle = Turtle("square")
            peddle.color("white")
            peddle.penup()
            peddle.setheading(90)
            peddle.goto(x=pos, y=0)
            peddle.shapesize(stretch_len=5, stretch_wid=1)
            self.peddles.append(peddle)

    def move_peddle_1_up(self):
        peddle_1 = self.peddles[0]
        peddle_1.forward(10)

    def move_peddle_2_up(self):
        peddle_2 = self.peddles[1]
        peddle_2.forward(10)

    def move_peddle_1_down(self):
        peddle_1 = self.peddles[0]
        peddle_1.backward(10)

    def move_peddle_2_down(self):
        peddle_1 = self.peddles[1]
        peddle_1.backward(10)
