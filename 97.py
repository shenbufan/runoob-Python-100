# -*- coding:UTF-8 -*-
file = open('string.txt','w')
while 1 :
	n = raw_input('please a char:')
	if n == '#':
		file.close()
		break
	else:
		file.write(n)

