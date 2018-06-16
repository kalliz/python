 try:
 n=int(input())
 s=str(input())
 l=s.split(" ")
 l2=[]
 for i in range(0,n):
  for j in range(i+1,n):
   if(int(l[i])==int(l[j])):
    l2.append(l[i])
 l1=[i for i in l if i not in l2]
 print(l1[0])
except:
 print("Invalid")
