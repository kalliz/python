s=str(raw_input())
print "real word : "+s
l=list(s)
l.sort()
s1=str(raw_input())
print "anagram word : "+s1
l1=list(s1)
l1.sort()
if(l==l1):
	print("anagram word")
else:
	print("not anagram word")
