string = 'clssssclssdewrclwjdcjwhdqllclwdclwdwclewcl'
s = 'cl'
n = 0
print string.count(s)#easy way
while string:
	j = string.find(s)
	if j == -1:
		break
	else:	
		string = string[j+len(s):]
		n+=1
print n


