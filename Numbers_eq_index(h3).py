try:
 n=int(input())
 s=str(input())
 l=s.split(" ")
 l1=[i for i in range(0,n) if(i==int(l[i]))]
 c=0
 st=""
 if(len(l1)>0):
  for i in l1:
   st=st+str(i)
   if(c!=len(l1)-1):
    st=st+" "
   c+=1
  print(st)
 else:
  print(-1)
except:
 print("Invalid")
