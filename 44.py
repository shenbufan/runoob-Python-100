# coding:UTF-8 #
x=[[12,7,3],[4,5,6],[7,8,9]]
y=[[5,8,1],[6,7,3],[4,5,9]]
z=[]
#for i in range(3):
	#z.append([])
#print z #test
#for i in range(3):
	#for j in range(3):
		#z[i].append(x[i][j]+y[i][j])
z0=[0,0,0]#这种操作导致了共享引用！！！！
z1=[0,0,0]
z2=[0,0,0]
#print z0,z1,z2 #test
for i in range(3):
	if i==0:
		for j in range(3):
			z0[j]=x[i][j]+y[i][j]
	elif i==1:
		for j in range(3):	
			z1[j]=x[i][j]+y[i][j]
	elif i==2:
		for j in range(3):
			z2[j]=x[i][j]+y[i][j]
z.append(z0)
z.append(z1)
z.append(z2)
print z
