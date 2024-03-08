import random

from src.constants import ENEMY_SPEED, MIN_HEADING_ANGLE, MAX_HEADING_ANGLE, ENEMY_ROTATION_ANGLE
from src.sprite import Sprite


class Enemy(Sprite):

    def __init__(self, sprite_shape, color, start_x, start_y):
        Sprite.__init__(self, sprite_shape, color, start_x, start_y)
        self.speed = ENEMY_SPEED
        self.setheading(random.randint(MIN_HEADING_ANGLE, MAX_HEADING_ANGLE))

    def turn_left(self):
        self.lt(ENEMY_ROTATION_ANGLE)

    def turn_right(self):
        self.rt(ENEMY_ROTATION_ANGLE)
