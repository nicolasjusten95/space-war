import random
import turtle

from src.sprite import Sprite


class Particle(Sprite):

    def __init__(self, sprite_shape, color, start_x, start_y):
        Sprite.__init__(self, sprite_shape, color, -1000, -1000)
        self.shapesize(stretch_wid=0.1, stretch_len=0.1, outline=None)
        self.frame = 0

    def explode(self, start_x, start_y):
        turtle.tracer(8)
        self.goto(start_x, start_y)
        self.setheading(random.randint(0, 360))
        self.frame = 1

    def move(self):
        if self.frame != 0:
            self.fd(18 - self.frame)
            self.frame += 1

        if self.frame < 6:
            self.shapesize(stretch_wid=0.3, stretch_len=0.3, outline=None)
        elif self.frame < 11:
            self.shapesize(stretch_wid=0.2, stretch_len=0.2, outline=None)
        else:
            self.shapesize(stretch_wid=0.1, stretch_len=0.1, outline=None)

        if self.frame > 18:
            self.frame = 0
            self.goto(-1000, -1000)
            turtle.tracer(0)
