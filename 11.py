# -*- coding:UTF-8 -*-
import time
x=int(raw_input('请输入第几个月：'))
print time.ctime()
def fib(n):
	if n==1 or n==2:
		return 1
	else:
		return fib(n-1)+fib(n-2)
print fib(x)
print time.ctime()