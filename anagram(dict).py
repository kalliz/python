s=str(input())
s=s.upper()
a = list(str(s))
s1=str(input())
s1=s1.upper()
b = list(str(s1))
d = {x:a.count(x) for x in a}
d1 = {x:b.count(x) for x in b}
print(d,d1)
if(d==d1):
 print("yes")
else:
 print("no")
