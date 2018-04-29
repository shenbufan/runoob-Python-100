#-*- coding:UTF-8 -*-
from Tkinter import *
import time
tk = Tk()
canvas = Canvas(tk,width=400,height=400)
canvas.pack()
canvas.create_oval(10,100,200,400)
tk.mainloop()