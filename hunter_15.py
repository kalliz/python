try:
	n=str(input())
	l=['saturday','sunday','monday','tuesday','wednesday','thursday','friday']
	m=n.lower()
	if m in l:
		print("yes")
	else:
		print("no")
except:
	print("error")
