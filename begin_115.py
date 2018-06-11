try:
	n=int(input())
	k=int(input())
	l=[]
	a=[]
	i=0
	for i in range(n):
		l.append(int(input()))
	l.sort()
	print(l[k-1])
except:
	print("error")
