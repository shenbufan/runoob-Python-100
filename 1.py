l=[]
for i in range(1,5):
	for j in range(1,5):
		for k in range(1,5):
			if (i!=j) and (i!=k) and(j!=k):
				print i j k
				l.append(i+j*10+k*100)
print l
