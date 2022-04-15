from turtle import Turtle

position = (0,0)
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.width = 20
        self.height = 20
        self.color('white')
        self.penup()
        self.goto(position)
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1
    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x , new_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1
        self.move_speed *= 0.9
    def goback(self):
        self.goto(position)
        self.x_move *= -1
        self.move_speed = 0.1