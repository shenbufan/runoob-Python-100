# -*- coding:UTF-8 -*-
def factorial(n):
	if n == 1:
		return 1
	elif n == 0:
		return 1
	elif n > 1:
		return n*factorial(n-1)
	else:
		return 'error'
print factorial(100)

def deadline(a,b,c,y,m,d):
	list =[31,28,31,30,31,30,31,31,30,31,30,31] 
	num = 0
	if (y-a)>1:
		for i in range(a+1,y):
				if i % 4==0:
					num+=1
		num = num + (y-a-1)*365#num现在等于去掉头尾两年的总天数	
		if b == 12:
			num = num + c
		else:
			for i in range(b,12):
				num = num +list[i]
			if (a%4==0) and (b<=2):
				num+=1
			num = num + list[b-1]-c
		if m == 1:
			num = num + d
		else:
			for i in range(m-1):
				num = num +list[i]
			if (y%4==0) and m>2:
				num+=1		
			num = num + d		
	elif y == a:
		if a%4==0 and b<=1:
			num+=1
		if b == m:
			num = d-c
		else:
			for i in range(b,m-1):
				num = num + list[i]
			num = num + list[b-1] - c + d
	elif y - a ==1:
		if b == 12:
			num = num + c
		else:
			for i in range(b,12):
				num = num +list[i]
			if (a%4==0) and (b<=2):
				num+=1
			num = num + list[b-1]-c
		if m == 1:
			num = num + d
		else:
			for i in range(m-1):
				num = num +list[i]
			if (y%4==0) and m>2:
				num+=1
			num = num + d
	return num
print deadline(2000,1,1,2017,12,11)


	




