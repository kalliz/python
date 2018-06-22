import itertools
try:
 s=str(input())
 s=s.upper()
 s1=str(input())
 s1=s1.upper()
 if(len(s)<=0 or len(s1)<0):
  print("Enter Valid imput")
 else:
  l1=list(s)
  m=[]
  l=list(itertools.permutations(l1))
  for i in range(len(l)):
   t=list(l[i])
   s=""
   for j in range(len(t)):
    s=s+t[j]
   m.append(s)
  x=0
  f=0
  while(f!=1 and x!=len(m)):
   if(m[x]==s1):
    print("This Is Anagram")
    f=1
    break
   x+=1
  if(f==0):
   print("This Not Anagaram")
except:
 print("Enter Valid imput")
