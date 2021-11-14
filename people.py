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
        self.x = x
        self.y = y
        self.h = h
        head = c.create_oval(x - h / 10, y, x + h / 10, y + h / 5)
        body = c.create_oval(x - h / 10, y + h / 5, x + h / 10, y + 3 * h / 5)
        footl = c.create_line(x - 5, y + 3 * h / 5, x - 20, y + h)
        footr = c.create_line(x + 5, y + 3 * h / 5, x + 20, y + h)
        handl = c.create_line(x - 8, y + h / 5 + 5, x - 30, y + 3 * h / 5)
        handr = c.create_line(x + 8, y + h / 5 + 5, x + 30, y + 3 * h / 5)

    def red(self):
        oval = c.create_oval(self.x - 2, self.y + 3 * self.h / 5 - 10, self.x + 2, self.y + 3 * self.h / 5)
        head = c.create_oval(self.x - self.h / 10, self.y, self.x + self.h / 10,
                             self.y + self.h / 5, fill="red")

def b1(event):
    root.title("Левая кнопка мыши")
    man1.red()

man1 = Man(50, 50, 100)
man2 = Man(100, 50, 120)
man3 = Man(150, 50, 70)

root.bind('<Button-1>', b1)




root.mainloop()
