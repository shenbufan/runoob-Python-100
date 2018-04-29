# -*- coding:UTF-8 -*-
x=raw_input('请输入第一个字母：')
if x=='M':
	print '星期一'
elif x=='T':
	y=raw_input('请输入第二个字母：')
	if y=='u':
		print '星期二'
	else:
		print '星期四'
elif x=='W':
	print '星期三'
elif x=='S':
	y=raw_input('请输入第二个字母：')
	if y=='a':
		print '星期六'
	else:
		print '星期天'
elif x=='F':
	print '星期五'
else:
	print 'ERROR!'
