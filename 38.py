# -*- coding:UTF-8 -*-
def f(l):
	sum=0
	for i in range(len(l)):
		sum+=int(l[i][i])
	return sum
s=[]
x=raw_input('请输入第一行：')
y=raw_input('请输入第二行：')
z=raw_input('请输入第三行：')
x=x.split(',')
y=y.split(',')
z=z.split(',')
print x,y,z
s.append(x)
s.append(y)
s.append(z)
print s
print len(s)
print f(s)

