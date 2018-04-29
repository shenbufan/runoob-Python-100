# -*- coding: UTF-8 -*-
"""
	函数f(n)计算n的平方，若平方小于50则退出
"""
TRUE=1
FALSE=0
again=1
def f(n):
	return n**2
while again:
	print'若输入的数结果大于50，则退出程序！'
	x=int(raw_input('请输入一个数：'))
	if f(x)>=50:
		print '运算结果为：%d'%(f(x))
		again=TRUE
	else:
		print '运算结果为：%d'%(f(x))
		again=FALSE
