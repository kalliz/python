# your code goes here
try:
 n=int(input())
 s=0
 while(n!=0):
  a=n%10
  s=s+a*a
  n=n//10
 print(s)
except:
 print("Invalid")
