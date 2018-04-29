# -*- coding:UTF-8 -*-
def f(n):
	l=[]
	for i in range(2,n+1):
		for j in range(2,i):
			if i%j==0:
				break
		else:#else语句块的缩进又出错！！！
			l.append(i)
	return l
print f(100)