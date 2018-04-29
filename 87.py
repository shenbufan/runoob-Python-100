# -*- coding :UTF-8 -*-
if __name__ == '__main__':
	class student:
		x = 0
		c = 0
	def f(stu):
		stu.x = 20
		stu.c = 10
	a = student()
	a.x = 3
	a.c = 'a'
	f(a)
	print a.x,a.c