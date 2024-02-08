import random
import turtle

from src.Enemy import Enemy
from src.Game import Game
from src.Missile import Missile
from src.Player import Player

# Configure turtle
turtle.fd(0)
turtle.speed(0)
turtle.bgcolor("black")
turtle.ht()
turtle.setundobuffer(1)
turtle.tracer(1)

# Create game object
game = Game()
game.draw_border()

# Create sprites
player = Player("triangle", "white", 0, 0)
enemy = Enemy("circle", "red", -100, 0)
missile = Missile("triangle", "yellow", 0, 0)


def fire_missile():
    missile.fire(player)


# Create keyboard bindings
turtle.onkey(player.turn_left, "Left")
turtle.onkey(player.turn_right, "Right")
turtle.onkey(player.accelerate, "Up")
turtle.onkey(player.decelerate, "Down")
turtle.onkey(fire_missile, "space")
turtle.listen()

# Main game loop
while True:
    player.move()
    enemy.move()
    missile.move()

    if player.is_collision(enemy):
        x = random.randint(-250, 250)
        y = random.randint(-250, 250)
        enemy.goto(x, y)

    if missile.is_collision(enemy):
        x = random.randint(-250, 250)
        y = random.randint(-250, 250)
        enemy.goto(x, y)
        missile.status = "ready"
