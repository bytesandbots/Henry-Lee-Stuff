from turtle import *
def drawing():
    forward(200)
    backward(100)
    left(90)
    forward(300)
    left(90)
    forward(200)
#head
def head():
    circle(20)
#left arm
def leftArm():
    left(90)
    forward(75)
    right(45)
    forward(50)
    right(180)
    forward(50)
#right arm
def rightArm():
    right(90)
    forward(50)
    right(180)
    forward(50)
#torso
def torso():
    left(135)
    forward(100)
#left leg
def leftLeg():
    right(45)
    forward(50)
    right(180)
    forward(50)
#right leg
def rightLeg():
    right(90)
    forward(50)
    right(180)
    forward(50)
    left(135)

