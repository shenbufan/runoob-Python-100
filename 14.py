# -*- coding: UTF-8 -*-
n=int(raw_input('请输入正整数：'))
def su(x):
	l=[]
	for i in range(2,x+1):
		for j in range(2,i):
			if i%j==0:
				break
		else:
			l.append(i)
	return l
def decouple(x):
	#l=su(x)
	s=[]
	print '%d='%x,
	while x>1:
		for i in range(2,x+1):
			if x%i==0:
				x=x/i
				s.append(i)
				break
	m=len(s)
	#print x,'=',这条语句不能放在这，此时x已被引用其他变量，应该放在while之前
	for i in range(m):
		if i!=m-1:
			print '%d *'%(s[i]),
		else:
			print '%d'%(s[i])
decouple(n)
