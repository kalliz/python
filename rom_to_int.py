rom=str(raw_input())
i=0
k=0
a=[]
while(i<len(rom)):
	if(rom[i]=='I'):
		a.append(1)
	elif(rom[i]=='X'):
		a.append(10)
	elif(rom[i]=='L'):
		a.append(50)
	elif(rom[i]=='C'):
		a.append(100)
	elif(rom[i]=='D'):
		a.append(500)
	elif(rom[i]=='M'):
		a.append(1000)
	else:
		print "Invalid"
	i=i+1
j=len(a)-1
k=a[j]
while(j>0):
	if(a[j]==a[j-1] or a[j]<a[j-1]):
		k=k+a[j-1]
	elif(a[j]>a[j-1]):
		k=k-a[j-1]
	else:
		pass
	j=j-1
print k	