# -*- coding:UTF-8 -*-
n=int(input("输入人数:"))
List=[]
for i in range(1,n+1):
    List.append(i)

sum=0
while 1:
    t=0;
    for i in range(1,len(List)+1):
    	print len(List),i
        sum=sum+1
        if (sum)%3==0:
            List.pop(i-1-t)
            t=t+1

    if len(List)==1:
        print("最后留下的是原来第%d号的那位" % List[0])
        break

