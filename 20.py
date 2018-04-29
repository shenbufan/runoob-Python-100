# -*-coding:UTF-8 -*-
n=1
x=100.0#参考了代码后，发现应该用浮点数表示长度，于是在数字后都加了.0
s=50.0
r=[150.0]
while n<10:
	x=s
	s=x/2
	l=x+s
	r.append(l)
	n+=1
print r
print sum(r[:9])+x #题目求的是第十次落地时经过了多少米，不包含回弹的距离
print s
