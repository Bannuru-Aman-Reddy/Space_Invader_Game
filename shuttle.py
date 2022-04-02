from random import randint
from turtle import Turtle
SHUTTLE_POSITIONS = [(-20, -275), (0, -275), (0, -255), (20, -275)]


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
        self.bullet_move_speed = 5
        create_line()

    def space_invader(self):
        self.create_booster(SHUTTLE_POSITIONS[0])
        self.create_shuttle(SHUTTLE_POSITIONS[1])
        self.create_shooter(SHUTTLE_POSITIONS[2])
        self.create_booster(SHUTTLE_POSITIONS[3])
        self.new_bullet()

    def create_shuttle(self, pos):
        shuttle = Turtle("circle")
        shuttle.color("white")
        shuttle.penup()
        shuttle.shapesize(1.5)
        shuttle.goto(pos)
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
        new_bullet.goto(self.shuttle[1].xcor(), self.shuttle[1].ycor()+23)
        self.bullets.append(new_bullet)

    def move_bullets(self):
        for bullet in self.bullets:
            new_ycor = bullet.ycor() + self.bullet_move_speed
            bullet.goto(bullet.xcor(), new_ycor)

    def remove_bullets(self):
        for bullet in self.bullets:
            if bullet.ycor() > 330:
                bullet.hideturtle()
                self.bullets.remove(bullet)

    def sb_stop(self):
        for bullet in self.bullets:
            bullet.goto(bullet.xcor(), bullet.ycor())

    def clear_sbc(self):
        for i in self.bullets:
            i.goto(1000, 1000)

    def sb_reset(self):
        self.clear_sbc()
        self.bullets.clear()
        for i in range(0, 4):
            self.shuttle[i].goto(SHUTTLE_POSITIONS[i])

