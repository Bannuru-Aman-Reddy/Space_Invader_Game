from turtle import Turtle, Screen
from shuttle import Shuttle, create_line, stars
from enemy import Enemy
from scoreboard import Scoreboard
import keyboard
import time


ALIGNMENT = "center"
FONT = ("Times New Roman", 15, "bold")


def erasable_write(tortoise, name, font, align, reuse=None):
    eraser = Turtle() if reuse is None else reuse
    eraser.color("white")
    eraser.hideturtle()
    eraser.up()
    eraser.setposition(tortoise.position())
    eraser.write(name, font=font, align=align)
    return eraser


my_screen = Screen()
my_screen.setup(600, 650)
my_screen.bgcolor("black")
my_screen.title("Space Invader")
my_screen.tracer(0)

shuttle = Shuttle()
enemy = Enemy()
scoreboard = Scoreboard()
create_line()

my_screen.listen()
my_screen.onkeypress(shuttle.left, "Left")
my_screen.onkeypress(shuttle.right, "Right")

LEVELS = {
    (0, 15): (1, enemy.enemy_gen_cor, shuttle.bullet_gen_cor),
    (15, 30): (2, enemy.enemy_gen_cor + 40, shuttle.bullet_gen_cor - 4),
    (30, 45): (3, enemy.enemy_gen_cor + 50, shuttle.bullet_gen_cor - 6),
    (45, 61): (4, enemy.enemy_gen_cor + 60, shuttle.bullet_gen_cor - 8)
}


game_time = False

stars()
my_screen.update()

rule = Turtle()
rule.color("white")
rule.hideturtle()
rule.penup()
rule.goto(0, 50)
er1 = erasable_write(rule, "LEVEL 1: 0+ KILLS", font=FONT, align=ALIGNMENT)
time.sleep(1)
er1.clear()
rule.goto(0, 25)
er2 = erasable_write(rule, "LEVEL 2: 15+ KILLS", font=FONT, align=ALIGNMENT)
time.sleep(0.9)
er2.clear()
rule.goto(0, 0)
er3 = erasable_write(rule, "LEVEL 3: 30+ KILLS", font=FONT, align=ALIGNMENT)
time.sleep(0.8)
er3.clear()
rule.goto(0, -25)
er4 = erasable_write(rule, "LEVEL 4: 45+ KILLS", font=FONT, align=ALIGNMENT)
time.sleep(0.8)
er4.clear()
rule.goto(0, -50)
er5 = erasable_write(rule, "LEVEL 5: 60+ KILLS", font=FONT, align=ALIGNMENT)
time.sleep(0.8)
er5.clear()
rule.goto(0, 0)
er6 = erasable_write(rule, "Press LEFT or RIGHT key to START", font=FONT, align=ALIGNMENT)
er6.clear()
rule.goto(500, 500)


while not game_time:
    if keyboard.is_pressed("left"):
        shuttle.left()
        game_time = True
    elif keyboard.is_pressed("right"):
        shuttle.right()
        game_time = True


while game_time:
    my_screen.update()
    time.sleep(0.08)

    # Game over
    if len(scoreboard.lives) == 0:
        scoreboard.game_over()
        game_time = False
        break

    for i, j in LEVELS.items():
        if scoreboard.score in range(i[0], i[1]) and scoreboard.score < 61:
            scoreboard.level = j[0]
            enemy.enemy_gen_cor = j[1]
            shuttle.bullet_gen_cor = j[2]
            scoreboard.update_scoreboard()

    if len(enemy.enemies) == 0 or enemy.enemies[-1].ycor() <= enemy.enemy_gen_cor:
        enemy.create_enemy()
    if shuttle.bullets[-1].ycor() >= shuttle.bullet_gen_cor or len(shuttle.bullets) == 0:
        shuttle.new_bullet()

    shuttle.move_bullets()
    enemy.move_enemy()
    # Detect Collision between bullet and an enemy
    for bullet in shuttle.bullets:
        for en in enemy.enemies:
            if en.distance(bullet) < 13:
                scoreboard.score += 1
                shuttle.bullets.remove(bullet)
                bullet.hideturtle()
                enemy.enemies.remove(en)
                en.hideturtle()
                scoreboard.update_scoreboard()

    # Detect if an enemy Crosses the line
    for eni in enemy.enemies:
        if eni.ycor() <= -235:
            eni.hideturtle()
            enemy.enemies.remove(eni)
            scoreboard.lives[-1].hideturtle()
            scoreboard.lives.remove(scoreboard.lives[-1])
            scoreboard.update_scoreboard()

    shuttle.remove_bullets()

my_screen.exitonclick()
