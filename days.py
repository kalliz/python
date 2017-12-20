s1=raw_input()
s=s1.lower()
if(s=='sunday'):
	print "false"
elif(s=='monday' or s=='tuesday' or s=='wednesday' or s=='thursday' or s=='friday' or s=='saturday'):
	print "true"
else:
	print "Invalid"
