class Node:
 def __init__(self,data=None,next_node=None):
  self.data=data
  self.next_node=next_node
 def get_next(self):
  return self.next_node
class link_list:
 def __init__(self):
  self.head=None
  self.first=None
 def add(self,data=None):
  self.head=Node(data,self.head)
 def print_list(self):
  curr=self.head
  while curr:
   print(curr.data,end='--> ')
   curr=curr.get_next()
 def search(self,data):
  curr=self.head
  f=0
  c=0
  while curr!=None:
   if curr.data==data:
    print("\n",data,"Found in :",c,"position")
    f=1
    break
   c+=1
   curr=curr.get_next()
  if(f!=1):
   print("\nNot found")
   
l=link_list()
li=[5,2,4,9,1]
print("\nThe List Is :")
for i in li:
 l.add(i)
l.print_list()
l.search(5)
