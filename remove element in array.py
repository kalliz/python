size=int(input())
s=str(input())
array1=s.split(" ")
array=[]
key=int(input())
for i in array1:
 array.append(int(i))
array.sort()
for i in range(len(array)):
 if(array[i]==key):
  index=i
  break
del array[index]
altered=""
count=0
for i in range(len(array)):
 altered+=str(array[i])
 if(count<len(array)-1):
  altered+=" "
 count+=1
print(altered)
