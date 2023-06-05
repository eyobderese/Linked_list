class Node:
  def __init__(self,data):
    self.data=data
    self.Next=None
    
    
class Linked_List:
  def __init__(self):
    self.count=0
    self.head=None
    self.tail=None
  def __isempity(self):
    return self.count==0
  def Itratethrough(self):
    curr=self.head
    while curr!=None:
      print(curr.data)
      curr=curr.Next
  def addLast(self,element):
    node=Node(element)
		self.count+1
    if self.head==None:
      self.head=self.tail=node
    self.tail.Next=node
    self.tail=node
	def searchItem(self,item):
		i=0
		current=self.head
		while current.data==item:
			if current==None:
				print("the item is not found")
				return -1
			current=current.Next
			i+=1
		return i
			
		
   
    
 
  
      
