l=[1,2,3,4,5]
x=1
l2=[]
l3=[]
l1=[]
for i in range(5):
 if(x==l[i]):
  lo=i
for i in range(0,lo):
 l3.append(l[i])
for i in range(lo+1,5):
 l2.append(l[i])
if(len(l3)>0):
 l1=l3[::-1]
e=0
e1=0
c=0
a=0
while(c!=3):
 if(a%2!=0 and e1<=len(l2)):
  print(l2[e])
  e+=1
  a=0
  c+=1
 elif(a%2==0 and e1<=len(l1)):
  print(l1[e1])
  e1+=1
  a=1
  c+=1
 elif(a%2==0 and e1>len(l1)):
  print(l2[e])
  e+=1
  a=1
  c+=1
 
