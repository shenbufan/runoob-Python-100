# -*- coding:UTF-8 -*-
from Tkinter import *
import time
root = Tk()
w = Canvas(root,width=500,height=500)
w.pack()
w.create_polygon(10,10,10,60,50,35)#id为1
for x in range(60):
	w.move(1,5,5)#第一个参数是id
	root.update()
	time.sleep(0.5)
root.mainloop()