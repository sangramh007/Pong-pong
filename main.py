from turtle import Screen
from partition import Partition
from peddle import Peddle
from ball import Ball
import time
from scoreboard import Score

screen = Screen()
screen.listen()
screen.bgcolor("black")
screen.setup(height=600, width=900)

partition = Partition()
partition.create_partition()
peddles = Peddle()
ball = Ball()
score = Score()
l_peddal = peddles.peddles[0]
r_peddal = peddles.peddles[1]
winning_score = 0

screen.onkeypress(peddles.move_peddle_1_up, 'q')
screen.onkeypress(peddles.move_peddle_2_up, 'p')
screen.onkeypress(peddles.move_peddle_1_down, 'a')
screen.onkeypress(peddles.move_peddle_2_down, 'l')

game_is_on = True

while game_is_on:
    screen.update()
    ball.move_ball()

    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.bounce_y()

    if ball.distance(r_peddal) < 50 and ball.xcor() > 340:
        ball.bounce_x()
    elif ball.xcor() > 430:
        ball.reset_game()
        score.update_score_player_1()

    if ball.distance(l_peddal) < 50 and ball.xcor() < -340:
        ball.bounce_x()
    elif ball.xcor() < -430:
        ball.reset_game()
        score.update_score_player_2()

    if score.player_1 > 9:
        partition.clear()
        ball.game_over("PLAYER 1")
        game_is_on = False
    elif score.player_2 == 10:
        partition.clear()
        ball.game_over("PLAYER 2")
        game_is_on = False
    else:
        pass

screen.exitonclick()
