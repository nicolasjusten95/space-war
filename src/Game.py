import turtle


class Game:

    def __init__(self):
        self.level = 1
        self.score = 0
        self.lives = 3
        self.state = "playing" # todo: define enum
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
        self.pen.ht()
