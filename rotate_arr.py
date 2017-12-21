try:
	a=[]
	n=int(raw_input())
	for i in range(0,n):
		x=int(raw_input())
		a.append(x)
	m=int(raw_input())
	b=len(a)
	d=[]
	c=len(a)-m
	for i in range (c,b):
		d.append(a[i])
	for i in range(0,c):
		if(len(d)!=b):
			d.append(a[i])
	print d
except:
	print "Invalid"
