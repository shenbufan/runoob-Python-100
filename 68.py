# -*- coding:UTF-8 -*-
import datetime
n = int(raw_input('请输入数组长度：'))
m = int(raw_input('请输入移动位数：'))
list = []
def List(num):
	for i in range(num):
		list.append(int(raw_input('请输入第%d个数:'%(i+1))))
	return list
def Move1(l,n):#Move1()是使用额外空间list_atmp存储超出长度的数
	t1 = datetime.datetime.now()
	length = len(l)
	list_atmp = []
	for i in range(length-1,-1,-1):
		if i+n > length-1:
			list_atmp.insert(0,l[i])
		else:
			l[i+n] = l[i]
	for i in range(len(list_atmp)):
		l[i] = list_atmp[i]
	global Move1_t #这里使用了全局变量 global
	Move1_t = datetime.datetime.now() - t1
	return l
def Move2(l,n):# Move2()增加了一个中间变量，节省了空间，但是有两重循环。
	t1 = datetime.datetime.now()
	for i in range(n):
		attmp = l[len(l)-1]
		for j in range(len(l)-2,-1,-1):
			l[j+1] = l[j]
		l[0] = attmp
	global Move2_t
	Move2_t = datetime.datetime.now() - t1
	return l
s1 = List(n)	
s2 = s1[:]
print s1
print Move1(s1,m)
print Move2(s2,m)
if Move2_t > Move1_t:
	print'choose 1'
else:
	print'choose 2'




