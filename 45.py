# -*- coding:UTF-8 -*-
"""
	定义函数f(n)计算1到n的和
"""
def f(n):
	sum=0
	for i in range(1,n+1):
		sum+=i
	return sum
print f(100)

