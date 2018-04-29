def peach(n):
	if n==1:
		return 1
	else:
		return (peach(n-1)+1)*2
print peach(10)