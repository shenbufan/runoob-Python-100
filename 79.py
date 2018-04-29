# -*- coding: UTF-8 -*-
s = 'ewuq8ue,r;l4pyw59689q2y435k02395AFHFHGFHFGUU&&GGfggGtu"][\kURESGjghfhGrNfn'
list = []
for i in s:
	list.append(ord(i))
print list
list.sort()
s_new = ''
for i in list:
	s_new = s_new + chr(i)
print s_new