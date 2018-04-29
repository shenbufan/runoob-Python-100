# -*- coding:UTF-8 -*-
x=int(raw_input('请输入不多于五位数的整数：'))
def f1(n,m):#不多于m位的正整数n
	for i in range(1,m+2):#调试的时候参数范围又出错
		if n/(10**i)==0:
			print i,
			break
def f2(s):
	print s[::-1]
l=str(x)
f1(x,5)
f2(l)