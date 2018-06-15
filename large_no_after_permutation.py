try:
 n=int(input())
 s=str(input()) 
 l=s.split(" ") 
 l2=[]
 l1=list(itertools.permutations(l))
 e=0
 for i in range(len(l1)):
  s=""
  for j in range(len(l1[i])):
   s=s+l1[i][j]
  l2.append(int(s))
 l2.sort(reverse=True)
 print(l2[0])
except:
 print("Invalid")
