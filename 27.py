#-*- coding:UTF-8 -*-
string=raw_input('请输入字符串：')
def f(s,n):
	if n==1:
		print s[0]
	else:
		print s[n-1],f(s[:n-1],n-1), 
f(string,len(string))


