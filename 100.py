# -*- coding:UTF-8 -*-
list1 = ['a','b','c','d','e','f']
list2 = ['angela','bob','candy','dad','eve','fb','gay']
dict = {}
l = min(len(list1),len(list2))
for i in range(l):
	dict[list1[i]] = list2[i]
print dict