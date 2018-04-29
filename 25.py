# -*- coding:UTF-8 -*-
def fun(n):#用递归实现阶乘
	if n==1:
		return 1
	else:
		return fun(n-1)*n
l=[]#用于存放1-20阶乘的值
for i in range(1,21):
	l.append(fun(i))
print l#用于调试
print sum(l)
print fun(5)