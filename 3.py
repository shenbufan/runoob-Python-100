# -*- coding: UTF-8 -*-
x=raw_input('请输入年：	')
y=raw_input('请输入月：	')
z=raw_input('请输入日：	')
day=0
arr=[31,28,31,30,31,30,31,31,30,31,30,31]
month=[2,3,4,5,6,7,8,9,10,11,12]
if int(y)==1:
	day=z
else: 
	for i in month:
		if int(y)==i:
			for j in range(i-1):
				day+=arr[j]
	day=day+int(z)
if int(x)%4==0 and int(y)>2:
	day+=1
print day 



