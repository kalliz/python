try:
	n=int(raw_input())
	sum=0
	c=0
	a=0
	while(n!=1):
		sum=0
		while(n>0):
			a=n%10
			sum=sum+(a*a)
			n=n/10
		if(sum==1):
			print "Happy Number"
			break
		n=sum
except:
	print "Invalid"
