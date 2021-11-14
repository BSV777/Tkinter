from tkinter import *

winwidth = 500
winheigh = 400

root = Tk()
root.title("")
root.resizable(False, False)

c = Canvas(root, width = winwidth, height = winheigh, bg = "white")
c.pack()



class Man:
    def __init__(self, x, y, h):
        head = c.create_oval(x - h / 10, y, x + h / 10, y + h / 5)
        body = c.create_oval(x - h / 10, y + h / 5, x + h / 10, y + 3 * h / 5)
        footl = c.create_line(x - 5, y + 3 * h / 5, x - 20, y + h)
        footr = c.create_line(x + 5, y + 3 * h / 5, x + 20, y + h)
        handl = c.create_line(x - 8, y + h / 5 + 5, x - 30, y + 3 * h / 5)
        handr = c.create_line(x + 8, y + h / 5 + 5, x + 30, y + 3 * h / 5)


man1 = Man(50, 50, 100)
man2 = Man(100, 50, 120)
man3 = Man(150, 50, 70)



root.mainloop()
