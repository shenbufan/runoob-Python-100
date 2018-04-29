# -*- coding:UTF-8 -*-
from Tkinter import *
root = Tk()
w = Canvas(root,width=500,height=500)
w.pack()
color=['#B53D3B','#375569','#B5C154','#FBCA41','#F5EDC2']
for i in range(1,25):
	j=w.create_rectangle(i*10,i*10,(49-i)*10,(49-i)*10)
	w.itemconfig(j,fill=color[i%5-1])
root.mainloop()