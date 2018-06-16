try:
 n=int(input())
 s=str(input())
 l=s.split(" ")
 l2=[]
 for i in range(0,len(l)):
  if(i%2==0 and int(l[i])%2!=0):
   l2.append(l[i])
  elif(i%2!=0 and int(l[i])%2==0):
   l2.append(l[i])
 c=0
 st=""
 for i in l2:
  st=st+str(i)
  if(c!=len(l2)-1):
   st=st+" "
   c+=1 

 print(st)
except:
 print("Invalid")
