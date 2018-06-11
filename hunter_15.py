try:
	n=str(input())
	l=['saturday','sunday','monday','tuesday','wednesday','thursday','friday']
	m=n.lower()
	if m==l[0] or m==l[1]:
		print("yes")
	else:
		print("no")
except:
	print("error")
