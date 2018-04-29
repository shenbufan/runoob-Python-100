# -*- coding:UTF-8 -*-
'''
Yh_List()返回第n行数字的列表
'''
def Yh_List(n):  
	if n==1:
		list=[1]
	elif n==2:
		list=[1,1]
	else:
		list= [1]
		for i in range(n-2):
			list.append((Yh_List(n-1))[i]+(Yh_List(n-1))[i+1])#递归效率真的好低
		list.append(1)
	return list
def Yh_Print(n):
	for i in range(1,n+1):
		print '  '*(n-i),
		for j in range(len(Yh_List(i))):
			if j==i-1:
				print Yh_List(i)[j]
			else:
				print (Yh_List(i))[j],' ',
Yh_Print(10)