try:
 n=int(input())
 s=str(input())
 l=s.split(" ")
 l1=[]
 f=0
 l2=[]
 for i in l:
  if(int(i)<0):
   l1.append(i)
 if(len(l1)>0):
  for i in l1:
   for j in l:
    if(abs(int(i))==int(j)):
     f=1
     l2.append(i)
     l2.append(j)
 if(f!=0):
  print(l2[0],l2[1])
 else:
  print(0,0)
except:
 print("Invalid")
