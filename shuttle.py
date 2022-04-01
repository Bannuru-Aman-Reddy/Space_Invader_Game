from random import randint
from turtle import Turtle
BOOSTER1_POSITION = (20, -275)
BOOSTER2_POSITION = (-20, -275)
SHOOTER_POSITION = (0, -255)


def stars():
    star = Turtle()
    star.color("white")
    star.penup()
    star.hideturtle()
    for i in range(150):
        star.penup()
        star.goto(randint(-330, 330), randint(-330, 330))
        star.pendown()
        for _ in range(5):
            star.pencolor("white")
            star.forward(3)
            star.right(144)


def create_line():
    line = Turtle()
    line.color("white")
    line.hideturtle()
    line.width(3)
    line.penup()
    line.goto(-300, -235)
    line.setheading(0)
    for i in range(30):
        line.pendown()
        line.forward(10)
        line.penup()
        line.forward(10)


class Shuttle:

    def __init__(self):
        self.shuttle = []
        self.bullets = []
        self.space_invader()
        self.bullet_gen_cor = -200
        create_line()

    def space_invader(self):
        self.create_shuttle()
        self.create_booster(BOOSTER1_POSITION)
        self.create_booster(BOOSTER2_POSITION)
        self.create_shooter((0, -255))
        self.new_bullet()

    def create_shuttle(self):
        shuttle = Turtle("circle")
        shuttle.color("white")
        shuttle.penup()
        shuttle.shapesize(1.5)
        shuttle.goto(0, -275)
        self.shuttle.append(shuttle)

    def create_booster(self, pos):
        booster = Turtle("square")
        booster.color("white")
        booster.penup()
        booster.shapesize(0.5)
        booster.goto(pos)
        self.shuttle.append(booster)

    def create_shooter(self, pos):
        shooter = Turtle("square")
        shooter.shapesize(stretch_len=0.7, stretch_wid=0.8)
        shooter.penup()
        shooter.color("white")
        shooter.goto(pos)
        self.shuttle.append(shooter)

    def left(self):
        for part in range(len(self.shuttle)):
            new_x = self.shuttle[part].xcor() - 13.5
            y_cor = self.shuttle[part].ycor()
            self.shuttle[part].goto(new_x, y_cor)

    def right(self):
        for part in range(len(self.shuttle)):
            new_x = self.shuttle[part].xcor() + 13.5
            y_cor = self.shuttle[part].ycor()
            self.shuttle[part].goto(new_x, y_cor)

    def new_bullet(self):
        new_bullet = Turtle("circle")
        new_bullet.shapesize(stretch_wid=0.5)
        new_bullet.penup()
        new_bullet.color("white")
        new_bullet.goto(self.shuttle[0].xcor(), self.shuttle[0].ycor()+23)
        self.bullets.append(new_bullet)

    def move_bullets(self):
        for bullet in self.bullets:
            new_ycor = bullet.ycor() + 5
            bullet.goto(bullet.xcor(), new_ycor)

    def remove_bullets(self):
        for bullet in self.bullets:
            if bullet.ycor() > 330:
                bullet.hideturtle()
                self.bullets.remove(bullet)
