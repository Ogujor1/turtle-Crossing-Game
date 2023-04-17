from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):

    def __init__(self):
      super().__init__()
      self.penup()
      self.shape("turtle")
      self.setheading(90)
      self.start_afresh()

    def move_up(self):
        self.forward(MOVE_DISTANCE)

    def start_afresh(self):
        self.goto(STARTING_POSITION)

    def successful_cross(self):
        if self.ycor() > 290:
            return True
        else:
            return False