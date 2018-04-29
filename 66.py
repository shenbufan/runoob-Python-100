# -*- coding:UTF-8 -*-
x = int(raw_input('请输入第一个数：'))
y = int(raw_input('请输入第二个数：'))
z = int(raw_input('请输入第三个数：'))
def Order(a,b,c):
	if b > a:
		a,b = b,a
	if c > a:
		a,c=c,a
	if c > b:
		c,b=b,c
	return a,b,c
print Order(x,y,z)
