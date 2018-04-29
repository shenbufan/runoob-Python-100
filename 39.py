# -*- coding:UTF-8 -*-
l=[1,2,3,10]
x=int(raw_input('please input one number:'))
def insert(n):
	l.append(x)
	if x<l[0]:
		for i in range(len(l)-2,-1,-1):
			l[i+1]=l[i]
		l[0]=x
		return l
	elif x>=l[len(l)-2]:
		return l
	else:
		for i in range(len(l)-2,-1,-1):
			if l[i]<=x:
				for j in range(len(l)-2,i,-1):
					l[j+1]=l[j]
				l[i+1]=x
				break
		return l
print insert(x)

