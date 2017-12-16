a='abcd'
b=len(a)
tot=0
avg=0
sum=0
for i in range (0,b):
	c=ord(a[i])
	sum=sum+c
avg=sum/b
print chr(avg)