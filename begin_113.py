# your code goes here
# your code goes here

try:
  n=int(input())
  k=int(input())
  l=[]
  c=0
  if(n>0):
	  for i in range(0,n):
	  	l.append(int(input()))
	  for x in l:
	  	if(x==k):
	  		c+=1
	  print(c)
  else:
 	  print("error")
except:
    print("error")
