try:
 n=int(input())
 s=str(input())
 l=s.split(" ")
 f=0
 e=0
 while(e!=n and f!=1):
  for i in range(e+1,n):
   if(l[e]==l[i]):
    x=l[e]
    f=1
    break
  e=e+1
 if(f!=0):
  print(x)
 else:
  print("unique")
except:
 print("Invalid")
