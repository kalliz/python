try:
 s1=str(input())
 l1=s1.split(" ")
 n=int(l1[1])
 s=str(input())
 l=s.split(" ")
 l.sort(reverse=True)
 print(l[n-1])
except:
 print("Invalid")
