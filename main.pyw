#import
import turtle
import random
import winsound
import webbrowser
from tkinter import *
import tkinter.messagebox

#tk
root = tkinter.Tk()
root.title("Main Menu")
root.geometry('400x450')
root.resizable(False, False)
bg = PhotoImage(file = "skin1.gif")
label1 = Label(root, image = bg)
label1.place(x = 0,y = -1)
label2= Label(root, image = bg)
label2.place(x = 0,y = 240)
def myth():
    tkinter.messagebox.showinfo("369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369",  "369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369 369" )
m=2
l = Label(root, text = "Gamemode is EASY", bg="#3355cc")
l.config(font =("Calibri", 14))
l.pack()
s=1
def skin1():
    global s
    global bg
    global label1
    global label2
    s=1
    bg = PhotoImage(file = "skin1.gif")
    label1 = Label(root, image = bg)
    label1.place(x = 0,y = -1)
    label2= Label(root, image = bg)
    label2.place(x = 0,y = 240)
    button = Button(root, text="Myth", command=myth, height=1, width=4)
    button.place(x=360, y=420)
    button = Button(root, text="Easy", command=ez, height=1, width=4)
    button.place(x=137, y=50)
    button = Button(root, text="Normal", command=norm, height=1, width=5)
    button.place(x=180, y=50)
    button = Button(root, text="Hard", command=hard, height=1, width=4)
    button.place(x=230, y=50)
    button = Button(root, text="START", command=root.destroy, height=1, width=10)
    button.place(x=160, y=150)
def skin2():
    global s
    global bg
    global label1
    global label2
    s=2
    bg = PhotoImage(file = "skin2.gif")
    label1 = Label(root, image = bg)
    label1.place(x = 0,y = -1)
    label2= Label(root, image = bg)
    label2.place(x = 0,y = 240)
    button = Button(root, text="Myth", command=myth, height=1, width=4)
    button.place(x=360, y=420)
    button = Button(root, text="Easy", command=ez, height=1, width=4)
    button.place(x=137, y=50)
    button = Button(root, text="Normal", command=norm, height=1, width=5)
    button.place(x=180, y=50)
    button = Button(root, text="Hard", command=hard, height=1, width=4)
    button.place(x=230, y=50)
    button = Button(root, text="START", command=root.destroy, height=1, width=10)
    button.place(x=160, y=150)
def skin3():
    global s
    global bg
    global label1
    global label2
    s=3
    bg = PhotoImage(file = "skin3.gif")
    label1 = Label(root, image = bg)
    label1.place(x = 0,y = -1)
    label2= Label(root, image = bg)
    label2.place(x = 0,y = 240)
    button = Button(root, text="Myth", command=myth, height=1, width=4)
    button.place(x=360, y=420)
    button = Button(root, text="Easy", command=ez, height=1, width=4)
    button.place(x=137, y=50)
    button = Button(root, text="Normal", command=norm, height=1, width=5)
    button.place(x=180, y=50)
    button = Button(root, text="Hard", command=hard, height=1, width=4)
    button.place(x=230, y=50)
    button = Button(root, text="START", command=root.destroy, height=1, width=10)
    button.place(x=160, y=150)
def skin4():
    global s
    global bg
    global label1
    global label2
    s=4
    bg = PhotoImage(file = "skin4.gif")
    label1 = Label(root, image = bg)
    label1.place(x = 0,y = -1)
    label2= Label(root, image = bg)
    label2.place(x = 0,y = 240)
    button = Button(root, text="Myth", command=myth, height=1, width=4)
    button.place(x=360, y=420)
    button = Button(root, text="Easy", command=ez, height=1, width=4)
    button.place(x=137, y=50)
    button = Button(root, text="Normal", command=norm, height=1, width=5)
    button.place(x=180, y=50)
    button = Button(root, text="Hard", command=hard, height=1, width=4)
    button.place(x=230, y=50)
    button = Button(root, text="START", command=root.destroy, height=1, width=10)
    button.place(x=160, y=150)
def about():
    tkinter.messagebox.showinfo("About","Made with fun by EnderMCDev")
def helpme():
    tkinter.messagebox.showinfo("Help","Choose Mode&Skin and press start.Your goal is reach as much point as possible by clicking the image")
def start():
    root.quit()
url="https://youtu.be/dQw4w9WgXcQ"
def rig():
    webbrowser.open_new_tab(url)  
def ez():
        global m
        m=2
        global l
        l.destroy()
        l = Label(root, text = "Gamemode is EASY", bg="#3355cc")
        l.config(font =("Calibri", 14))
        l.pack()
def norm():
        global m
        m=5
        global l
        l.destroy()
        l = Label(root, text = "Gamemode is NORMAL", bg="#3355cc")
        l.config(font =("Calibri", 14))
        l.pack()
def hard():
        global m
        m=10
        global l
        l.destroy()
        l = Label(root, text = "Gamemode is HARD", bg="#3355cc")
        l.config(font =("Calibri", 14))
        l.pack()
button = Button(root, text="Myth", command=myth, height=1, width=4)
button.place(x=360, y=420)
button = Button(root, text="Easy", command=ez, height=1, width=4)
button.place(x=137, y=50)
button = Button(root, text="Normal", command=norm, height=1, width=5)
button.place(x=180, y=50)
button = Button(root, text="Hard", command=hard, height=1, width=4)
button.place(x=230, y=50)
button = Button(root, text="START", command=root.destroy, height=1, width=10)
button.place(x=160, y=150)

menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Easy", command=ez)
filemenu.add_command(label="Normal", command=norm)
filemenu.add_command(label="Hard", command=hard)
menubar.add_cascade(label="Difficulty", menu=filemenu)

skinmenu = Menu(menubar, tearoff=0)
skinmenu.add_command(label="VK(Default)", command=skin1)
skinmenu.add_command(label="VK1", command=skin2)
skinmenu.add_command(label="test", command=skin3)
skinmenu.add_command(label="AMOGUS", command=skin4)
menubar.add_cascade(label="Skin", menu=skinmenu)

helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="Help", command=helpme)
helpmenu.add_command(label="DO NOT CLICK", command=rig)
helpmenu.add_command(label="Myth", command=myth)
helpmenu.add_command(label="About", command=about)
menubar.add_cascade(label="Help", menu=helpmenu)
root.config(menu=menubar)
root.mainloop()
#screen
wn=turtle.Screen ()
wn.title(0)
wn.bgcolor("black")
turtle.register_shape('skin1.gif')
turtle.register_shape('skin2.gif')
turtle.register_shape('skin3.gif')
turtle.register_shape('skin4.gif')
wn.setup(1000,700)
winsound.PlaySound("main.wav", winsound.SND_ASYNC | winsound.SND_LOOP)
n=0
wn.title(n)
#asset

sq=turtle.Turtle()
if (s==1):
    sq.shape("skin1.gif")
if (s==2):
    sq.shape("skin2.gif")
if (s==3):
    sq.shape("skin3.gif")
if (s==4):
    sq.shape("skin4.gif")
sq.shapesize(50,50)
sq.penup()
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
        sq.onclick(fxn)
