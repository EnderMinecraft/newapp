#import
import turtle
import random
import winsound
from tkinter import *

#tk
m=2
def ez():
        global m
        m=2
def norm():
        global m
        m=5
def hard():
        global m
        m=10
root = Tk()
menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Easy", command=ez)
filemenu.add_command(label="Normal", command=norm)
filemenu.add_command(label="Hard", command=hard)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="Gamemode", menu=filemenu)


root.config(menu=menubar)
root.mainloop()
#screen
wn=turtle.Screen ()
wn.title(0)
wn.bgcolor("black")
turtle.register_shape('place.gif')
wn.setup(1000,700)
winsound.PlaySound("main.wav", winsound.SND_ASYNC | winsound.SND_LOOP)
n=0
wn.title(n)
#asset

sq=turtle.Turtle()
sq.shape("place.gif")
sq.shapesize(100,100)

sq.speed(m)

#boundnclk
xin=random.randint(0, 7)
yin=random.randint(0, 3)
while True:
        def fxn(a, b):
                global n
                a=random.randint(-300,10)
                b=random.randint(10,300)
                sq.setposition(a,b)
                n=n+1
                turtle.title(n)
        x=sq.xcor()
        y=sq.ycor()
        x=x+xin
        y=y+yin
        sq.setposition(x,y)
        if (x==300 or x==-300):
            xin=xin*-0.4
        if (y==400 or y==-400):
            yin=yin*-0.6
        sq.onclick(fxn, btn=1)
Tk.destroy()
