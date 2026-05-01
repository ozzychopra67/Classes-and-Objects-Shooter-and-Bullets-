from turtle import *
import random

def generate_color():
    return f"#{random.randint(0, 0xFFFFFF):06x}"

def playing_area():
    pen = Turtle()
    pen.ht()
    pen.speed(0)
    pen.color('light blue')
    pen.begin_fill()
    pen.goto(-240,240)
    pen.goto(240,240)
    pen.goto(240,-240)
    pen.goto(-240,-240)
    pen.goto(-240,240)
    pen.end_fill()
    
class Head(Turtle):

  def __init__(self, screen, body):
    super().__init__()
    self.shape("square")
    self.color("black")
    self.pu()
    self.goto(0,0)
    self.alive = True
    screen.onkey(self.up,"Up")
    screen.onkey(self.down, "Down")
    screen.onkey(self.left, "Left")
    screen.onkey(self.right, "Right")

  def up(self):
    if self.heading() != 270:
      self.setheading(90)


  def down(self):
    if self.heading() != 90:
      self.setheading(270)

  def left(self):
    if self.heading() != 0:
      self.setheading(180)


  def right(self):
    if self.heading() != 180:
      self.setheading(0)

  def die(self):
    self.alive = False

  def move(self):
    self.forward(20)
    if self.xcor() > 240 or self.xcor() < -240:
      self.ht()
      self.die(self)
    elif self.ycor() > 240 or self.ycor() < -240:
      self.ht()
      self.die(self)


class Segment(Turtle):
  def __init__(self, other):
    super().__init__()
    pass

  def move(self, other):
    pass

class Apple(Turtle):
  def __init__(self):
    super().__init__()
    pass

  def relocate(self):
    pass

screen = Screen()
screen.bgcolor("black")
screen.setup(520,520)
# Key Binding. Connects key presses and mouse clicks with function calls
screen.listen()
playing_area()
body = []


screen.exitonclick()






screen.exitonclick()
