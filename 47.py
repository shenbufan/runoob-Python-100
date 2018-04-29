# -*- coding: UTF-8 -*-
'''
	swap
'''
def f(a,b):
	a,b=b,a
	return a,b
x=raw_input('请输入变量a：')
v1=raw_input('请输入变量a的值：')
y=raw_input('请输入变量b：')
v2=raw_input('请输入变量b的值：')
x=v1
y=v2
print f(x,y)
