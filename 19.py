#-*- coding:UTF-8 -*-
s=[]#存放完数
for i in range(1,1001):
	l=[]
	for j in range(1,i):#错误1:把范围设成了包含自身range(1,i+1)，自然结果就出错。
		if i%j==0:
			#i=i/j 错误2:此乃求质数算法
			l.append(j)
	print l#用于测试,找bug
	print sum(l)#用于测试，找bug
	if sum(l)==i:
		s.append(i)
print s
