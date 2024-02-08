import turtle

from src.Constants import MAX_GAME_BORDER, MIN_GAME_BORDER


class Sprite(turtle.Turtle):

    def __init__(self, sprite_shape, color, start_x, start_y):
        turtle.Turtle.__init__(self, shape=sprite_shape)
        self.speed(0)
        self.penup()
        self.color(color)
        self.fd(0)
        self.goto(start_x, start_y)
        self.speed = 1

    def move(self):
        self.fd(self.speed)

        if self.xcor() > MAX_GAME_BORDER:
            self.setx(MAX_GAME_BORDER)
            self.rt(60)

        if self.xcor() < MIN_GAME_BORDER:
            self.setx(MIN_GAME_BORDER)
            self.rt(60)

        if self.ycor() > MAX_GAME_BORDER:
            self.sety(MAX_GAME_BORDER)
            self.rt(60)

        if self.ycor() < MIN_GAME_BORDER:
            self.sety(MIN_GAME_BORDER)
            self.rt(60)

    def is_collision(self, other):
        if (self.xcor() >= (other.xcor() - 20)) and \
                (self.xcor() <= (other.xcor() + 20)) and \
                (self.ycor() >= (other.ycor() - 20)) and \
                (self.ycor() <= (other.ycor() + 20)):
            return True
        return False
