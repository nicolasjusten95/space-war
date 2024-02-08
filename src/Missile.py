from enum import Enum

from src.Constants import MIN_MOVEMENT_BORDER, MAX_MOVEMENT_BORDER, MISSILE_SPEED
from src.Sprite import Sprite


class Missile(Sprite):

    def __init__(self, sprite_shape, color, start_x, start_y):
        Sprite.__init__(self, sprite_shape, color, start_x, start_y)
        self.shapesize(stretch_wid=0.2, stretch_len=0.4, outline=None)
        self.speed = MISSILE_SPEED
        self.status = MissileState.READY

    def fire(self):
        if self.status == MissileState.READY:
            self.status = MissileState.SHOOT

    def move_missile(self, player):
        if self.status == MissileState.READY:
            self.hideturtle()
            self.goto(-1000, 1000)

        if self.status == MissileState.SHOOT:
            self.goto(player.xcor(), player.ycor())
            self.setheading(player.heading())
            self.showturtle()
            self.status = MissileState.FIRING

        if self.status == MissileState.FIRING:
            self.fd(self.speed)

        if self.xcor() < MIN_MOVEMENT_BORDER or self.xcor() > MAX_MOVEMENT_BORDER \
                or self.ycor() < MIN_MOVEMENT_BORDER or self.ycor() > MAX_MOVEMENT_BORDER:
            self.status = MissileState.READY


class MissileState(Enum):
    READY = 1
    SHOOT = 2
    FIRING = 3
