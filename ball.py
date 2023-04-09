from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = 10
        self.y_move = 10

    def move_ball(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1

    def reset_game(self):
        self.clear()
        self.goto(0, 0)

    def game_over(self, player):
        self.goto(0, 0)
        self.hideturtle()
        self.pendown()
        self.write(f"GAME OVER : {player} WON!", align="center", font=('Arial', 20, 'normal'))
