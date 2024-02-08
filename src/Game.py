import turtle
from enum import Enum


class Game:

    def __init__(self):
        self.level = 1
        self.score = 0
        self.state = GameState.SPLASH
        self.lives = 3
        self.pen = turtle.Turtle()

    def draw_border(self):
        self.pen.speed(0)
        self.pen.color("white")
        self.pen.pensize(3)
        self.pen.penup()
        self.pen.goto(-300, 300)
        self.pen.pendown()
        for side in range(4):
            self.pen.fd(600)
            self.pen.rt(90)
        self.pen.penup()

    def show_status(self):
        self.pen.undo()
        if self.lives > 0:
            msg = "Level: %s Lives: %s Score: %s" % (self.level, self.lives, self.score)
        else:
            msg = "Game Over! Score: %s" % self.score
        self.pen.penup()
        self.pen.goto(-300, 300)
        self.pen.write(msg, font=("Arial", 16, "normal"))


class GameState(Enum):
    SPLASH = 1
    PLAYING = 2
    RESTART = 3
    GAME_OVER = 4
