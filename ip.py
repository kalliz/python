try:
	s=str(raw_input())
	n=len(s)-1
	m=len(s)
	c=0
	x=0
	f=str()
	i=0
	if m<=12:
		while(x!=1):
			if(i==m):
				x=1
				break
			elif(c==3):
				f=f+'.'
				c=0
				i=i-1
				pass
			elif(i!=s[n]):
				f=f+s[i]
				c=c+1
			i=i+1
	else:
		print "Invalid"
	print f
except:
	print "Invalid"
