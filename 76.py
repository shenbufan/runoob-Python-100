# -*- coding:UTF-8 -*-
def f(n):
	result = 0
	if n%2 == 0:
		for i in range(2,n+1,2):
			result = result + 1.0/i# Python里，整数除整数，只能得出整数，所以需要使用 浮点数 1.0
	else:
		for i in range(1,n+1,2):
			result = result + 1.0/i
	return result
print f(3)
print f(2)
