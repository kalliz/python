try:
	string=raw_input()
	if(int(string)>0):
		print int(string)
	else:
		print "cannot convert to integer"
except:
	print "cannot convert to integer"
