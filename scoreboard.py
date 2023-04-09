from turtle import Turtle

POSITIONS = [(-80, 250), (80, 250)]
ALIGNMENT = "center"
FONT = ('Arial', 20, 'normal')


class Score():

    def __init__(self):
        self.scores = []
        self.player_1 = 0
        self.player_2 = 0
        self.create_scoreboard()

    def create_scoreboard(self):
        for pos in POSITIONS:
            player = Turtle()
            player.color("white")
            player.hideturtle()
            player.penup()
            player.goto(pos)
            player.write("SCORE: 0", align=ALIGNMENT, font=FONT)
            self.scores.append(player)

    def update_score_player_1(self):
        score_1 = self.scores[0]
        self.player_1 += 1
        score_1.clear()
        score_1.goto(POSITIONS[0])
        score_1.write(f"SCORE: {self.player_1}", align=ALIGNMENT, font=FONT)

    def update_score_player_2(self):
        score_2 = self.scores[1]
        self.player_2 += 1
        score_2.clear()
        score_2.goto(POSITIONS[1])
        score_2.write(f"SCORE: {self.player_2}", align=ALIGNMENT, font=FONT)
