try:
	s1=str(raw_input())
	s=s1[::-1]
	a=str()
	print s
	n=len(s)
	for i in range(0,n):
		if(s[i]=='a' or s[i]=='e' or s[i]=='i' or s[i]=='o' or s[i]=='u'):
			i=i+1
			pass
		else:
			a=a+s[i]
	print a
except:
	print "Invalid"
