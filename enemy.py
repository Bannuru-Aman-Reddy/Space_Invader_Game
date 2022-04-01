from turtle import Turtle
from random import randint


class Enemy:

    def __init__(self):
        self.enemies = []
        self.create_enemy()
        self.enemy_gen_cor = 100
        self.levels = [10, 20, 30, 40, 50]

    def create_enemy(self):
        new_enemy = Turtle(shape="triangle")
        new_enemy.setheading(270)
        new_enemy.penup()
        new_enemy.goto(randint(-280, 280), 335)
        new_enemy.color("white")
        self.enemies.append(new_enemy)

    def move_enemy(self):
        for enemy in self.enemies:
            new_ycor = enemy.ycor() - 10
            enemy.goto(enemy.xcor(), new_ycor)
