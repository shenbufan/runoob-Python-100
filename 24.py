a=[2.0]
b=[1.0]
c=[2/1]
for i in range(19):
	b.append(a[i])
	a.append(a[i]+b[i])
	c.append(a[i+1]/b[i+1])
print c
print len(c)
print sum(c)




