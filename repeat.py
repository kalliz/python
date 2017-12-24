try:
	s1=str(raw_input())
	g=str()
	max=0
	s=s1.split(' ')
	n=len(s)
	a=[]
	for i in range (0,n):
		a.append(0)
	for i in range(0,n):
		m=len(s[i])
		for j in range(0,m):
			for k in range (0,m):
				if(j!=k):
						if(s[i][j]==s[i][k]):
							g=g+(s[i][j])
							a[i]=a[i]+1
	v=0
	max=a[0]
	for i in range (0,len(a)):
	    if(a[i]>=max):
		max=a[i]
		v=i
	print s[v]
except:
	print "Invalid"
