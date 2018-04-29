# -*- coding:UTF-8 -*-
dict = {'Li':12,'M':54,'d':56,'ty':3}
m = dict['Li']
for i in dict.keys():
	if dict[i] > m:
		m = dict[i]
		key = i 
print 'name:',key,'age:',m