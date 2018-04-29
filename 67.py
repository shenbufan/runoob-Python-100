# -*- coding:UTF-8 -*-
n = int(raw_input('请输入数组长度：'))
#函数array()用于输入数组元素
def array(num):
	list = []
	for i in range(num):
		m = int(raw_input('请输入第%d个数'%(i+1)))
		list.append(m)
	return list
	
#maxinum()用于找出列表最大数的索引值，为了锻炼算法，拒绝使用内置函数实现
def maxinum(l):
	a = l[0]
	index = 0
	for i in range(1,len(l)):
		if l[i] > a:
			a = l[i]
			index = i
	l[0],l[index] = l[index],l[0]


def mininum(l):
	b = l[0]
	index = 0
	for i in range(1,len(l)):
		if l[i] < b:
			b = l[i]
			index = i
	l[len(l)-1],l[index] = l[index],l[len(l)-1]


s = array(n)
maxinum(s)#先
mininum(s)#后
print s

