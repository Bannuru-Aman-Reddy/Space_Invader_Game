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
stars()

LEVELS = {
    (0, 15): (1, 125, 8, 7),
    (15, 30): (2, 150, 11, 10),
    (30, 45): (3, 180, 15, 14),
    (45, 61): (4, 210, 19, 18),
    (61, 75): (5, 250, 24, 23)
}


def execute():
    game_time = False
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
    time.sleep(0.8)
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
            shuttle.sb_stop()
            enemy.enemy_stop()
            scoreboard.game_over()
            rule.goto(0, 25)
            for i in range(10, -1, -1):
                er7 = erasable_write(rule, f"Game restarts in {i} secs", font=("Times New Roman", 18, "bold"), align=ALIGNMENT)
                time.sleep(1)
                er7.clear()
            enemy.reset_enemy()
            shuttle.sb_reset()
            rule.goto(500, 500)
            scoreboard.score = 0
            scoreboard.create_lives()
            scoreboard.update_scoreboard()
            execute()
        # LEVELS = {
        #     (0, 15): (1, 100, -200, 8, 7),
        #     (15, 30): (2, 140, -205, 10, 10),
        #     (30, 45): (3, 150, -208, 12, 13),
        #     (45, 61): (4, 160, -210, 15, 17)
        # }

        for i, j in LEVELS.items():
            if scoreboard.score in range(i[0], i[1]+1) and scoreboard.score < 75:
                scoreboard.level = j[0]
                enemy.enemy_gen_cor = j[1]
                enemy.enemy_move_Speed = j[2]
                shuttle.bullet_move_speed = j[3]
                scoreboard.update_scoreboard()

        if len(enemy.enemies) == 0 or enemy.enemies[-1].ycor() <= enemy.enemy_gen_cor:
            enemy.create_enemy()
        if len(shuttle.bullets) == 0 or shuttle.bullets[-1].ycor() >= shuttle.bullet_gen_cor:
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

execute()

my_screen.exitonclick()
