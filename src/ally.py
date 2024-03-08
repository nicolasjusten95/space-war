import random

from src.constants import MAX_MOVEMENT_BORDER, MIN_MOVEMENT_BORDER, MIN_HEADING_ANGLE, MAX_HEADING_ANGLE, ALLY_SPEED, \
    ALLY_ROTATION_ANGLE, ALLY_AVOID_BOX
from src.sprite import Sprite


class Ally(Sprite):

    def __init__(self, sprite_shape, color, start_x, start_y):
        Sprite.__init__(self, sprite_shape, color, start_x, start_y)
        self.speed = ALLY_SPEED
        self.setheading(random.randint(MIN_HEADING_ANGLE, MAX_HEADING_ANGLE))

    def move(self):
        self.fd(self.speed)

        if self.xcor() > MAX_MOVEMENT_BORDER:
            self.setx(MAX_MOVEMENT_BORDER)
            self.lt(ALLY_ROTATION_ANGLE)

        if self.xcor() < MIN_MOVEMENT_BORDER:
            self.setx(MIN_MOVEMENT_BORDER)
            self.lt(ALLY_ROTATION_ANGLE)

        if self.ycor() > MAX_MOVEMENT_BORDER:
            self.sety(MAX_MOVEMENT_BORDER)
            self.lt(ALLY_ROTATION_ANGLE)

        if self.ycor() < MIN_MOVEMENT_BORDER:
            self.sety(MIN_MOVEMENT_BORDER)
            self.lt(ALLY_ROTATION_ANGLE)

    def avoid(self, other):
        if (self.xcor() >= (other.xcor() - ALLY_AVOID_BOX)) and \
                (self.xcor() <= (other.xcor() + ALLY_AVOID_BOX)) and \
                (self.ycor() >= (other.ycor() - ALLY_AVOID_BOX)) and \
                (self.ycor() <= (other.ycor() + ALLY_AVOID_BOX)):
            self.lt(ALLY_ROTATION_ANGLE / 2)
