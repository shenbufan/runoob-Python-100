#-*- coding:UTF-8 -*-
import math
l=[]#l作为符合条件的素数
for i in range(101,201):
	for j in range(2,int(math.sqrt(i))+1):
		if i%j==0:
			break
	else:
		l.append(i)
print l
print len(l)
	