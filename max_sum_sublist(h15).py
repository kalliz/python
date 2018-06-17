import itertools
try:
 n=int(input())
 st=str(input())
 l=st.split(" ")
 l1=[]
 for i in range(1,len(l)+1):
  l1.append(list(itertools.combinations(l,i)))
 max=0
 for i in range(len(l1)):
  l2=list(l1[i])
  for j in range(len(l2)):
   n=0
   l3=list(l2[j])
   for k in range(len(l3)):
    n=n+int(l3[k])
   if(max<n):
    max=n
 print(max)
except:
 print("Invalid")
