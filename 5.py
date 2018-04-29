# -*- coding: UTF-8 -*-
x=int(raw_input('输入x：'))
y=int(raw_input('输入y：'))
z=int(raw_input('输入z：'))
l=[x,y,z]
swap=0
while l:
	for i in range(len(l)-2):
		if l[i]>l[i+1]:
			swap=l[i]
			l[i]=l[i+1]
			l[i+1]=swap
		print l[0]
		l=l[1:]
