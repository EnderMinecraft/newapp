#import
import turtle
import random
import winsound

#screen
wn=turtle.Screen ()
wn.title("Temp")
wn.bgcolor("black")
turtle.register_shape('place.gif')
winsound.PlaySound("main.wav", winsound.SND_ASYNC | winsound.SND_LOOP)

#asset
sq=turtle.Turtle()
sq.shape("place.gif")
sq.shapesize(100,100)
#boundnclk
xin=random.randint(0, 7)
yin=random.randint(0, 3)
while True:
        def fxn(a, b):
            a=random.randint(-300,10)
            b=random.randint(10,300)
            sq.setposition(a,b)
            winsound.PlaySound("click.wav", winsound.SND_ASYNC | winsound.SND_NOSTOP)
        x=sq.xcor()
        y=sq.ycor()
        x=x+xin
        y=y+yin
        sq.setposition(x,y)
        if (x==400 or x==-400):
            xin=xin*-0.4
        if (y==200 or y==-200):
            yin=yin*-0.5
        sq.onclick(fxn)
