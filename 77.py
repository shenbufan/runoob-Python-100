# -*- coding:UTF-8 -*-
l = [1,2,3,4,5,6,7,8,9]
n = 20
while n>0:
	for i in l:
		print i,
	for i in range(len(l)-2,0,-1):
		print l[i],
	n-=1