try:
 s=str(input())
 l=s.split(" ")
 l.sort()
 st=""
 c=0
 for i in l:
  st=st+str(i[::-1])
  if(c!=len(l)-1):
   st=st+" "
   c+=1
 print(st)
except:
 print("Invalid")
