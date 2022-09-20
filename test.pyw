import turtle
import random
import winsound

#screen
wn=turtle.Screen ()
wn.title("test")
wn.bgcolor("black")
turtle.register_shape("place.gif")
winsound.PlaySound("main.wav", winsound.SND_ASYNC)

#main
sq=turtle.Turtle()
sq.shape("place.gif")
sq.shapesize(100,100)
turtle.penup

xin=random.randint(0, 7)
yin=random.randint(0, 3)

while True:
        x=sq.xcor()
        y=sq.ycor()
        x=x+xin
        y=y+yin
        sq.setposition(x,y)
        if (x==400 or x==-400):
            xin=xin*-0.4
        if (y==200 or y==-200):
            yin=yin*-0.5
