# -*- coding: UTF-8 -*-
s = 0
for i in range(1,100):
	if '8' not in str(i) and '9'not in str(i):
		if i % 2 != 0:
			print i,
			s+=1
print s
