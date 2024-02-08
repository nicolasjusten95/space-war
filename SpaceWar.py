import random
import time
import turtle
from tkinter import messagebox

from src.Ally import Ally
from src.Constants import INITIAL_PLAYER_SPEED
from src.Enemy import Enemy
from src.Game import Game, GameState
from src.Missile import Missile, MissileState
from src.Particle import Particle
from src.Player import Player

# Configure turtle
turtle.fd(0)
turtle.speed(0)
turtle.bgcolor("black")
turtle.bgpic("src/media/starfield.gif")
turtle.title("Space War")
turtle.ht()
turtle.setundobuffer(1)
turtle.tracer(0)

# Create game object
game = Game()
game.draw_border()
game.show_status()

# Create sprites
player = Player("triangle", "white", 0.0, 0.0)
missile = Missile("triangle", "yellow", 0.0, 0.0)
enemies = []
allies = []
particles = []

# Create keyboard bindings
turtle.onkey(player.turn_left, "Left")
turtle.onkey(player.turn_right, "Right")
turtle.onkey(player.accelerate, "Up")
turtle.onkey(player.decelerate, "Down")
turtle.onkey(missile.fire, "space")
turtle.listen()

if game.state == GameState.SPLASH:
    for p in range(2):
        particles.append(Particle("circle", "yellow", -1000, -1000))
    for p in range(2):
        particles.append(Particle("circle", "red", -1000, -1000))
    for p in range(2):
        particles.append(Particle("circle", "orange", -1000, -1000))

    game.state = GameState.RESTART


def on_collision(other):
    player.color("red")
    for particle in particles:
        particle.explode(other.xcor(), other.ycor())
    player.rt(random.randint(100, 200))
    other.reset_to_random_position()
    other.speed += 1
    game.lives -= 1
    print("Hit! Lives left: %s" % game.lives)
    if game.lives < 1:
        game.state = GameState.GAME_OVER
    game.show_status()
    player.color("white")


def on_missile_collision(other):
    for particle in particles:
        particle.explode(other.xcor(), other.ycor())
    missile.status = MissileState.READY
    other.reset_to_random_position()
    other.speed += 1


# Main game loop
while True:
    turtle.update()
    time.sleep(0.02)

    if game.state == GameState.RESTART:
        print("Restarting Game")
        game.lives = 3
        game.score = 0
        player.speed = INITIAL_PLAYER_SPEED
        player.goto(0, 0)
        player.setheading(0)
        x = random.randint(-200, 200)
        y = random.randint(-200, 200)
        enemies.append(Enemy("circle", "red", x, y))
        x = random.randint(-200, 200)
        y = random.randint(-200, 200)
        allies.append(Ally("square", "blue", x, y))

        for enemy in enemies:
            enemy.speed = random.randint(1, game.level)
        for ally in allies:
            ally.speed = random.randint(1, game.level)

        game.state = GameState.PLAYING

    if game.state == GameState.PLAYING:
        player.move()
        missile.move_missile(player)

        for enemy in enemies:
            enemy.move()
            if player.is_collision(enemy):
                on_collision(enemy)
            if missile.is_collision(enemy):
                on_missile_collision(enemy)
                game.show_status()
                game.score += 100
                print("Score: %s" % game.score)
                if game.score == (game.level * 200):
                    game.state = GameState.LEVEL_UP

        for ally in allies:
            ally.move()
            for enemy in enemies:
                ally.avoid(enemy)
            ally.avoid(player)
            if player.is_collision(ally):
                on_collision(ally)
            if missile.is_collision(ally):
                on_missile_collision(ally)
                game.score -= 100
                game.show_status()

        for particle in particles:
            particle.move()

        if game.state == GameState.GAME_OVER:
            for i in range(360):
                player.rt(1)
            print("Game Over!")
            messagebox.showinfo("Game Over", "Level reached: %s" % game.level)
            exit()

        if game.state == GameState.LEVEL_UP:
            game.level += 1
            print("Level up: %s" % game.level)
            game.state = GameState.RESTART

