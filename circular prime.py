mm=str(input())
ll=mm.split(" ")
n=int(ll[0])
n1=int(ll[1])
def prime(n):
 c=0
 k=n
 for j in range(1,k+1):
  if(n%j==0):
   c=c+1
 if(c==2):
  return(True)
l=[]
for i in range(n,n1+1):
 if(prime(i)==True):
  l.append(i)
fin=""
m=0
l1=[]
for i in range(len(l)):
 s=str(l[i])
 if(prime(int(s[::-1]))==True):
  l1.append(str(l[i]))
l1.sort()
for i in range(len(l1)):
 fin=fin+l1[i]
 if(m<len(l1)-1):
  fin=fin+" "
  m+=1
print(fin)
