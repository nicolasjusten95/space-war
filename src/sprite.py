import random
import turtle

from src.constants import MAX_MOVEMENT_BORDER, MIN_MOVEMENT_BORDER, SPRITE_DEFAULT_ROTATION_ANGLE, SPRITE_HIT_BOX


class Sprite(turtle.Turtle):

    def __init__(self, sprite_shape, color, start_x, start_y):
        turtle.Turtle.__init__(self, shape=sprite_shape)
        self.speed(0)
        self.penup()
        self.color(color)
        self.fd(0)
        self.goto(start_x, start_y)
        self.speed = 0

    def move(self):
        self.fd(self.speed)

        if self.xcor() > MAX_MOVEMENT_BORDER:
            self.setx(MAX_MOVEMENT_BORDER)
            self.rt(SPRITE_DEFAULT_ROTATION_ANGLE)

        if self.xcor() < MIN_MOVEMENT_BORDER:
            self.setx(MIN_MOVEMENT_BORDER)
            self.rt(SPRITE_DEFAULT_ROTATION_ANGLE)

        if self.ycor() > MAX_MOVEMENT_BORDER:
            self.sety(MAX_MOVEMENT_BORDER)
            self.rt(SPRITE_DEFAULT_ROTATION_ANGLE)

        if self.ycor() < MIN_MOVEMENT_BORDER:
            self.sety(MIN_MOVEMENT_BORDER)
            self.rt(SPRITE_DEFAULT_ROTATION_ANGLE)

    def reset_to_random_position(self):
        self.goto(random.randint(-200, 200), random.randint(-200, 200))

    def is_collision(self, other):
        if (self.xcor() >= (other.xcor() - SPRITE_HIT_BOX)) and \
                (self.xcor() <= (other.xcor() + SPRITE_HIT_BOX)) and \
                (self.ycor() >= (other.ycor() - SPRITE_HIT_BOX)) and \
                (self.ycor() <= (other.ycor() + SPRITE_HIT_BOX)):
            return True
        return False
