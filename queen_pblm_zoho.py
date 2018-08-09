def search(l):
	m=[]
	i=0
	while(i<len(l)):
		if(l[i]==1):
			m.append(l[i])
		elif(l[i]!=2 and i<n//2+1):
			m=[]
			while(l[i]==1 or l[i]==2):
				if(l[i]==1):
					m.append(l[i])
				i+=1
		i+=1
	return(len(m))
n=5
l=[]
for i in range(n):
	for j in range(n):
		li=[1,1,1,1,1]
		l.append(li)
for i in range(n):
	for j in range(n):
		#queen position
		if(i==2 and j==2):
			l[i][j]=2
		#obstacle position
		if(i==0 and j==3):
			l[i][j]=0
		#if(i==4 and j==2):
		#	l[i][j]=0
for i in range(n):
	print(' '.join([str(i) for i in l[i]]))
#for i in range(n):
l_diag=[l[i][i] for i in range(n)]
r_diag=[]
top=[]
left=[]
e=0
main=[]
for j in range(n-1,-1,-1):
	r_diag.append(l[e][j])
	e+=1
for i in range(n):
	left.append(l[2][i])
for i in range(n):
	top.append(l[i][2])
#print(l_diag,r_diag,left,top)
sum=search(top)+search(l_diag)+search(r_diag)+search(left)
print(sum)
