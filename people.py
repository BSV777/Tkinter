from tkinter import *

winwidth = 500
winheigh = 400

root = Tk()
root.title("")
root.resizable(False, False)

c = Canvas(root, width = winwidth, height = winheigh, bg = "white")
c.pack()



oval = c.create_oval(20, 20, 40, 40)

line = c.create_line(50, 50, 70, 70)





root.mainloop()
