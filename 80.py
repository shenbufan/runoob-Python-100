# -*- coding: UTF-8 -*-
end = 100
i1 = 0
while i1 ==0:
	end = end*2
	for i5 in range(6,end):
		if (i5-1)%5 == 0:
			if i5%4 == 0:
				i4 = i5/4*5+1
				if i4%4 == 0:
					i3 = i4/4*5+1
					if i3%4 == 0:
						i2 = i3/4*5+1
						if i2%4 == 0:
							i1 =i2/4*5+1
							print i1
							break

