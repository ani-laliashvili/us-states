from turtle import Turtle

class Answer(Turtle):
    def __init__(self, x, y, name):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(x, y)
        self.write(name, font= ("Arial",12,"normal"), align="center", move=False)

