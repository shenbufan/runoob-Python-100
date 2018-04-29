# -*- coding:UTF -*-
import random
list = []
for i in range(7):
	list.append(random.randint(1,50))
for i in list:
	print '*' * i,i
