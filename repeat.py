s1=str(raw_input())
g=str()
s=s1.split(' ')
n=len(s)
for i in range(0,n):
	m=len(s[i])
	c=0
	for j in range(0,m):
		for k in range (1,m):
			if(j!=k):
				f=s[i][j]
				if(f!=1):
					if(s[i][j]==s[i][k]):
						g=g+(s[i][j])
						f=1
				else:
					c=c+1
print g
print c
