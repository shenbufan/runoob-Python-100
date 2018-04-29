# -*- coding:UTF-8 -*-
l=[1,2,8,4,4,54,68,25,16,6]
s=[1,4,7,9,2,5,7,0,3,7,7,9]
n=[-1,2,-53,0,4,3,4,6]
p=[0.2,0.4,1.2,-0.3,-0.3,0]
def kuaisu(x):
	m=[x[0]]#用于存放已排好序的数，从小到大排序
	#print m#测试
	n=len(x)
	#print n#测试
	i=1
	while i<n:
		if x[i]>=m[i-1]:#将x中当前元素与有序列表m最后一个元素进行比较，如果大于则插入m。i加1
			m.append(x[i])
			i+=1
			#print 'm',m,i#测试
		elif x[i]<m[0] :#之前漏掉了这个情况，如果x[i]比m中最小值还要小的情况
					m.append(0)
					for k in range(len(m)-1,0,-1):
						m[k]=m[k-1]
					m[0]=x[i]
					i+=1
					#print m,i#test
		else:#如果x中当前元素比m中最后一个元素小或相等，那么就将x[i]与m倒序逐一比较，直到找到m[j]<=x[i]为止。把m[j+1]-m[len(m)]逐一后移，再插入m[j+1]
			#print 'else'#测试
			for j in range(len(m)-1,-1,-1):#这里注意range(i,j)中是从i开始但不包含j，所以这里需要-1
				if x[i]>=m[j]:
					m.append(0)#用于使m长度增1，不然会报index out of range
					for k in range(len(m)-1,j+1,-1):
						m[k]=m[k-1]
					m[j+1]=x[i]
					i+=1
					#print m,i#test
					break
	return m 
print kuaisu(l)
print kuaisu(s)
print kuaisu(n)
print kuaisu(p)


