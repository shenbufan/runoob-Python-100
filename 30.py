# -*- coding:UTF-8 -*-
x=str(int(raw_input('请输入：')))
def f(s,n):
		for i in range(n/2):
			if s[i]!=s[n-1-i]:
				return 'No'
		else:#在第一版本中，并没有加入else模块，导致逻辑错误，输出有误！！
			return 'yes'				
print f(x,len(x))

