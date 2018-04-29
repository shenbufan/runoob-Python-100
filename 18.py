# -*- coding:UTF-8 -*-
x=int(raw_input('请输入a：'))
y=int(raw_input('请输入个数：'))
l=[]
def f1(m,n):
	for j in range(1,n+1):
		r=0#这条语句应该放在循环内，每一次都把前一次的结果清零。
		for i in range(j):
			#a=m*10**i
			r=r+m*10**i
		l.append(r)
		if i==n-1:
			print r,'=',
		else:
			print r,'+',
	print sum(l)
	print l
f1(x,y)


