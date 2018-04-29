#-*- coding:UTF-8 -*-
from Tkinter import *
root = Tk()
w = Canvas(root,width=400,height=400)
w.pack()
for i in range(100):
	w.create_rectangle(10+i,40+i,344-i,288-i,outline='red')
	w.create_oval(250+i,250+i,250-i,250-i)
root.mainloop()