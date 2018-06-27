s=str(input())
count=0
count1=0
f=0
for i in range(len(s)):
 if(s[i]=='('):
   count+=1
 elif(s[i]==')'):
   count1+=1
 else:
   print("no")
   f=1
   break
if(f==0):
 if(count==count1):
  print("yes")
 else:
  print("no")
