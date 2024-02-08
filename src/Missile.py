from src.Constants import MIN_GAME_BORDER, MAX_GAME_BORDER
from src.Sprite import Sprite


class Missile(Sprite):

    def __init__(self, sprite_shape, color, start_x, start_y):
        Sprite.__init__(self, sprite_shape, color, start_x, start_y)
        self.shapesize(stretch_wid=0.3, stretch_len=0.4, outline=None)
        self.speed = 20
        self.status = "ready"  # todo: define enum
        self.move_off_screen()

    def fire(self, player):
        if self.status == "ready":
            self.goto(player.xcor(), player.ycor())
            self.setheading(player.heading())
            self.status = "firing"

    def move(self):
        if self.status == "ready":
            self.move_off_screen()
        if self.status == "firing":
            self.fd(self.speed)
        if self.xcor() < MIN_GAME_BORDER or self.xcor() > MAX_GAME_BORDER or self.ycor() < MIN_GAME_BORDER or self.ycor() > MAX_GAME_BORDER:
            self.move_off_screen()
            self.status = "ready"

    def move_off_screen(self):
        self.goto(-1000, 1000)
