try:
  n=int(input())
  k=int(input())
  l=[]
  a=[]
  c=0
  if(n>0):
	  for i in range(0,n):
	  	l.append(int(input()))
	  a=[x for x in l if(x%2!=0)]
	  print(a[k-1])
  else:
 	  print("error")
except:
    print("error")
