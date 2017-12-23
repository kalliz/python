try:
	c=0
	n=str(raw_input())
	a=[]
	for i in range (0,len(n)):
		a.append(n[i])
	if len(n)%2==0:
		j=len(n)
	else:
		j=len(n)-1
	while(c!=j):
		t=a[c]
		a[c]=a[c+1]
		a[c+1]=t
		c=c+2
	print a
except:
	print "Invalid"
