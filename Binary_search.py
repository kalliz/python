s=str(input())
s1=str(input())
l=s.split(" ")
l1=s1.split(" ")
key=int(l[1])
first=0
n=int(l[0])
last=n-1
mid=round((first+last)/2)
f=0
while(first<=last and f==0):
 if(int(l1[mid])==key):
  print("Yes")
  f=1
  break
 elif(key<int(l1[mid])):
  last=mid-1
 else:
  first=mid+1
 mid=round((first+last)/2)
if(f==0):
 print("No")
