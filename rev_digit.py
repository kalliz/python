try:
	n=int(raw_input())
	a=0
	sum=0
	x=n
	while(n!=0):
		a=n%10
		sum=sum*10+a
		n=n/10
	print sum
		
except:
	print "Error"
