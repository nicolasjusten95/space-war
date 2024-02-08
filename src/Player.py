from src.Constants import PLAYER_ROTATION_ANGLE, PLAYER_ACCELERATION, INITIAL_PLAYER_SPEED
from src.Sprite import Sprite


class Player(Sprite):

    def __init__(self, sprite_shape, color, start_x, start_y):
        Sprite.__init__(self, sprite_shape, color, start_x, start_y)
        self.shapesize(stretch_wid=0.6, stretch_len=1.1, outline=None)
        self.speed = INITIAL_PLAYER_SPEED

    def turn_left(self):
        self.lt(PLAYER_ROTATION_ANGLE)

    def turn_right(self):
        self.rt(PLAYER_ROTATION_ANGLE)

    def accelerate(self):
        self.speed += PLAYER_ACCELERATION

    def decelerate(self):
        self.speed -= PLAYER_ACCELERATION
