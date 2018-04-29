s=['a','b','c']
l=['x','y','z']
m=[]
d={}
for i in s:
	for j in l:
		if i=='c' and j!='x'and j!='z':
			d[i]=j
			m.append(j)
		if i=='a' and j!='x' and j not in m:
			d[i]=j
			m.append(j)
for k in l:
	if k  not in m:
		d['b']=k
print d