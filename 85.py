# -*- coding: UTF-8 -*-
number = raw_input('please input an odd:')
end = len(number)
flag = 0
while flag == 0:
	dividend = 0
	for i in range(end):
			dividend += 9*(10**i) 
			if dividend % (int(number)) == 0:
				print dividend
				flag = 1
				break
	end = end*2

		
