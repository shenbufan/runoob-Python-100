# -*- coding:UTF-8 -*-
from Tkinter import *
root = Tk()
w = Canvas(root,width=500,height=500)
w.pack()
w.create_line(0,0,500,500,fill='red')
w.create_line(0,0,0,500,fill='blue')#相当于y轴不能显示
w.create_line(0,0,500,0,fill='blue')#相当于x轴不能显示
w.create_line(0,500,500,500,fill='blue')
w.create_line(500,0,500,500,fill='blue')
root.mainloop()