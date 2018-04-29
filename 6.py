# -*- coding: UTF-8 -*-
def fibonacci(n):
	while n>2:
		return fibonacci(n-2)+fibonacci(n-1)
	return 1
print fibonacci(10)