a=[]
n=int(raw_input())
for i in range (0,n):
    x=int(raw_input())
    a.append(x)
b=[]
c=[]
for i in range(0,len(a)):
    c.append(0)
#b.append(a[0])
for i in range(0,len(a)):
    f=0
    for j in range(0,len(b)):
        if(b[j]==a[i]):
            c[j]=c[j]+1
            i=i+1
            f=1
    if(f!=1):
        b.append(a[i])
min=c[0]
v=0
for j in range(0,len(b)):
        if(c[j]<min):
            min=c[j]
            v=j
print b[v]
