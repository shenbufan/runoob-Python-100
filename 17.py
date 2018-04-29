# -*- coding:UTF-8 -*-
s=raw_input('请输入字符串：')
num=[]
word=[]
char=[]
none=[]
for i in s:
	k=ord(i)
	if 47<k<58:
		num.append(i)
	elif 64<k<107 or 96<k<123:
		word.append(i)
	elif k==32:
		none.append(i)
	else:
		char.append(i)
print '英文字母个数：',len(word)
print '空格数：',len(none)
print '数字个数：',len(num)
print '其他字符数：',len(char)
