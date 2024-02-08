import random
import turtle

from src.Enemy import Enemy
from src.Game import Game
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

# Create keyboard bindings
turtle.onkey(player.turn_left, "Left")
turtle.onkey(player.turn_right, "Right")
turtle.onkey(player.accelerate, "Up")
turtle.onkey(player.decelerate, "Down")
turtle.listen()

# Main game loop
while True:
    player.move()
    enemy.move()

    if player.is_collision(enemy):
        x = random.randint(-250, 250)
        y = random.randint(-250, 250)
        enemy.goto(x, y)
