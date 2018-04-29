# -*- coding:UTF-8 -*-
number = list(raw_input('please input :'))#注意！输入的是字符串，而字符串是不允许变的！！
#所以应该转换为列表或者是使用一个另外的列表
for i in range(4):
	number[i] = (int(number[i])+5) % 10
	#number[i] = (ord(number[i]) - ord('0') + 5) % 10
for i in range(2):
	number[i],number[3-i] = number[3-i],number[i]
print number

