from turtle import *
import random

def generate_color():
    return f"#{random.randint(0, 0xFFFFFF):06x}"

def playing_area():
    pen = Turtle()
    pen.ht()
    pen.speed(0)
    pen.color('teal')
    pen.begin_fill()
    pen.goto(-240,240)
    pen.goto(240,240)
    pen.goto(240,-240)
    pen.goto(-240,-240)
    pen.goto(-240,240)
    pen.end_fill()
    
class Player(Turtle):
    def __init__(self, x, y, color, screen, right_key, left_key, fire_key, health):
        super().__init__()
        self.ht()
        self.speed(0)
        self.color(color)
        self.penup()
        self.goto(x,y)
        self.setheading(90)
        self.shape("turtle")
        self.bullets = []
        self.hue = color
        self.alive = True
        self.health = health
        self.st()
        screen.onkeypress(self.turn_left, left_key)
        screen.onkeypress(self.turn_right, right_key)
        screen.onkey(self.fire, fire_key)

    def turn_left(self):
        self.left(10)

    def turn_right(self):
        self.right(10)

    def move(self):
        self.forward(4)
        if self.xcor() > 230 or self.xcor() < -230:
            self.setheading(180 - self.heading())
        if self.ycor() > 230 or self.ycor() < -230:
            self.setheading(-self.heading())

    def fire(self):
        self.bullets.append(Bullet(self))

class Bullet(Turtle):
    def __init__(self, player):
        super().__init__()
        self.ht()
        self.speed(0)
        self.pu()
        self.setheading(player.heading())
        self.color(player.hue)
        self.goto(player.xcor(), player.ycor())
        self.player = player
        self.st()

    def move_bullet(self):
        self.forward(10)
        if self.xcor() > 230 or self.xcor() < -230:
            self.ht()
            self.player.bullets.remove(self)
        if self.ycor() > 230 or self.ycor() < -230:
            self.ht()
            self.player.bullets.remove(self)
    
    def die(self):
        self.ht()
        self.player.bullets.remove(self)
    





screen = Screen()
screen.bgcolor("black")
screen.setup(520,520)

screen.listen()


playing_area()

p1 = Player(-100, 0, "red",screen, "d", "a", "w",3)
p2 = Player(100,0,"blue",screen, "Right","Left", "Up",3)

while p1.alive and p2.alive:
    p1.move()
    p2.move()
    for bullet in p1.bullets:
        bullet.move_bullet()
        if bullet.distance(p2) < 20:
            bullet.die()
            p2.health -= 1
            if p2.health == 2:
                p2.color("yellow")
            elif p2.health == 1:
                p2.color("red")
            elif p2.health == 0:
                p2.ht()
                p2.alive = False
            

    for bullet in p2.bullets:
        bullet.move_bullet()
        if bullet.distance(p1) < 20:
            bullet.die()
            p1.health -= 1
            if p1.health == 2:
                p1.color("yellow")
            elif p1.health == 1:
                p1.color("red")
            elif p1.health == 0:
                p1.ht()
                p1.alive = False



screen.exitonclick()