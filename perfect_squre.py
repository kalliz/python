try:
 s=str(input())
 l=s.split(" ")
 min=int(l[0])
 max=int(l[1])
 count=0
 for i in range(min,max+1):
  y=i**(.5)
  z=round(y)
  if(y%z==0):
   count+=1
 print(count)
except:
 print("Invalid")
