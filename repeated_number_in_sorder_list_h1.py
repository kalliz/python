try:
 n=int(input())
 l=[]
 l1=[]
 s=str(input())
 l=s.split(" ")
 for i in range(n):
  for j in range(n):
   if(i!=j):
    if(l[i]==l[j]):
     f=1
     l1.append(l[i])
 lis=set(l1)
 ll=[]
 for i in lis:
  ll.append(i)
 ll.sort()
 str=""
 c=0
 for i in ll:
  str=str+i
  if(c<len(ll)-1):
   str=str+" "
  c+=1
 if(f==1):
  print(str)
 else:
  print("unique")
except:
 print("Invalid")
