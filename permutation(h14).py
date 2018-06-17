import itertools
try:
 st=str(input())
 l1=list(st)
 l2=[]
 l=list(itertools.permutations(l1))
 for i in range(0,len(l)):
  s=""
  for j in range(0,len(l[i])):
   s=s+str(l[i][j])
  l2.append(s)
 l3=set(l2)
 for i in l3:
  print(i)
except:
 print("Invalid")
