from turtle import Turtle
ALIGNMENT = "left"
FONT = ("Times New Roman", 15, "bold")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.lives = []
        self.level = 1
        self.xcor = -220
        self.ycor = -300
        self.score = 0
        self.high_score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.create_lives()
        self.update_scoreboard()

    def read_high_score(self):
        with open("high_score.txt", "r") as hs:
            self.high_score = hs.read()

    def create_lives(self):
        for i in range(0, 81, 20):
            new_life = Turtle("square")
            new_life.color("white")
            new_life.penup()
            new_life.shapesize(0.75)
            new_life.goto(self.xcor+i, self.ycor)
            self.lives.append(new_life)

    def update_scoreboard(self):
        self.clear()
        self.goto(-295, -312)
        self.write(fr"LIVES: ", align=ALIGNMENT, font=FONT)
        self.goto(190, -312)
        self.write(fr"SCORE: {self.score}", align=ALIGNMENT, font=FONT)
        self.goto(0, -312)
        self.write(fr"LEVEL={self.level}", align="center", font=FONT)

    def game_over(self):
        self.goto(0, 50)
        self.write("GAME OVER!!", align="center", font=("Times New Roman", 20, "bold"))
        self.goto(0, 0)
        self.write(fr"YOUR SCORE: {self.score}", align="center", font=FONT)
        self.goto(0, -25)
        if self.score > int(self.high_score):
            with open("high_score.txt", "w") as high_score:
                high_score.write(f"{self.score}")
            self.write(fr"HIGH SCORE: {self.high_score}", align="center", font=FONT)
        else:
            self.write(fr"HIGH SCORE: {self.high_score}", align="center", font=FONT)
        self.read_high_score()
