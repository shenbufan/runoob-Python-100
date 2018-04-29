import copy
def exchange1(l,s):
	s=l[:]
	return s
def exchange2(l,s):
	for i in range(min(len(l),len(s))):
		s[i]=l[i]
	return s
def exchange3(l,s):
	s=copy.copy(l)
	return s
