a=str(input())
l=list(a)
s="("
s1="("
for i in range(len(l)):
 s=s+l[i]
 s1=s1+l[i]
 if(i<len(l)-1):
  s=s+"+"
  s1=s1+"*"
s=s+")"
s1=s1+")"
s2=s+"*"+s1
print(s2)
