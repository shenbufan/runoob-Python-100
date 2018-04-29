# -*- coding:UTF-8 -*-
from turtle import *
t = Pen()
t.circle(10)
for i in range(1,10):
	t.penup()
	t.goto(0,(-5)*i)
	t.pendown()
	t.circle((5)*(i+2))


