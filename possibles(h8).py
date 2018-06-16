try:
 n=int(input())
 s=str(input())
 l=s.split(" ")
 for i in range(n):
  for j in range(i+1,n):
   for k in range(j+1,n):
    if int(l[i])+int(l[j])==int(l[k]):
     if(i<j):
      print(l[i],l[j],l[k])
except:
 print('Invalid')
