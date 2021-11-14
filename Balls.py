from tkinter import *
import random

winwidth = 500
winheigh = 400

numballs = random.randint(1, 7)
balls = []
radius = 10
timems = 50

def motion():  
    global balls
    for b in balls:
        c.move(b[0], b[1], b[2])

        x = c.coords(b[0])[0] + radius
        y = c.coords(b[0])[1] + radius

        if (x <= radius or x >= winwidth - radius):
            b[1] *= -1
        if (y <= radius or y >= winheigh - radius):
            b[2] *= -1
    root.after(timems, motion)

root = Tk()
root.title("")
root.resizable(False, False) 

c = Canvas(root, width = winwidth, height = winheigh, bg = "white")
c.pack()

for i in range(numballs):
    startx = random.randint(radius * 5, winwidth - radius * 5)
    starty = random.randint(radius * 5, winheigh - radius * 5)
    dx = random.randint(-radius, radius)
    dy = random.randint(-radius, radius)
    balls.append([c.create_oval(startx - radius, starty - radius, startx + radius, starty + radius, fill='green'), dx, dy])

motion()
root.mainloop()
