try:
	n=int(raw_input())
	a=[]
	for i in range (0,n):
		x=int(raw_input())
		a.append(x)
	l=len(a)-1
	i=0
	c=0
	f=0
	p=a[0]
	while(c!=l):
		if(a[p]==a[l]):
			f=1
			print "true"
			break
		else:
			i=i+p
			p=a[i]
			c=c+1
	if(f==0):
		print "false"
except:
	print "Invalid"
