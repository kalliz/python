# your code goes here
try:
 l=int(input())
 s=str(input())
 a=""
 for i in range(l):
  if(s[i]=="a" or s[i]=="e" or s[i]=="i" or s[i]=="o" or s[i]=="u"):
   pass
  else:
   a=a+s[i]
 b=a[::-1]
 print(b)
except:
 print("Invalid")
