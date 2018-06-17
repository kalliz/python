try:
 so=str(input())
 ns=so.split(" ")
 n=int(ns[0])
 n1=int(ns[1])
 s=str(input())
 l=s.split(" ")
 s1=str(input())
 l1=s1.split(" ")
 f=1
 e=0
 while(f!=0 and e!=n1):
  for i in l1:
   if i in l:
    e=e+1
   else:
    f=0
    break
 if(f!=0):
  print("YES")
 else:
  print("NO") 
except:
 print("Invalid")
