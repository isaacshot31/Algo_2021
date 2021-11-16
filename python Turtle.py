import random
import turtle

maTortue = turtle.Turtle()
maTortue1 = turtle.Turtle()
maTortue2 = turtle.Turtle()
maTortue.speed(10)
maTortue1.speed(10)
maTortue2.speed(10)
maTortue.color("red")
maTortue1.color("green")
maTortue2.color("blue")
maTortue.sety(random.randint(-100,100))
maTortue.setx(random.randint(-100,100))
maTortue1.sety(random.randint(-100,100))
maTortue1.setx(random.randint(-100,100))
maTortue2.sety(random.randint(-100,100))
maTortue2.setx(random.randint(-100,100))
maTortue.shape('turtle')
maTortue1.shape('turtle')
maTortue2.shape('turtle')
import random




"""
"exo 1"
maTortue.speed(1)
maTortue.forward(90)
maTortue.left(90)
maTortue.forward(90)
maTortue.left(90)
maTortue.forward(90)
maTortue.left(90)
maTortue.forward(90)
"""

"""""
for i in range(190):
 maTortue.forward(1)
 maTortue.right(1)
 maTortue.forward(90)
 maTortue.left(90)
"""""

"""""escargot  carrer devoir
x=1
while 1==1:
    x+=1
    maTortue.right(90)
    maTortue.forward(x)
"""

""""" escargot rond
x=1
while 1==1:
    x+=1
    maTortue.right(10)
    maTortue.forward(x)
"""

""" ligne infinie
x=1
while 1==1:
    x+=1
    turtle.right(0)
    turtle.forward(x)"""
maTortue.penup()
maTortue1.penup()
maTortue2.penup()
maTortue.shapesize(random.randint(1,20)) 
maTortue1.shapesize(random.randint(1,20)) 
maTortue2.shapesize(random.randint(1,20)) 
for i in range(200):
    maTortue.left(random.randint(-100,100))
    maTortue.forward(random.randint(0,50))
    maTortue1.left(random.randint(-100,100))
    maTortue1.forward(random.randint(0,50))
    maTortue2.left(random.randint(-100,100))
    maTortue2.forward(random.randint(0,50))

input()