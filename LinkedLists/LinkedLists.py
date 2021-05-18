class Node:
	def __init__(self,data):
		self.data=data
		self.next=None

class LinkedList:
	def __init__(self):
		self.head=None                  
		
	def traverse(self):
		current=self.head
		while current is not None:
			print(current.data,end=' ')
			current=current.next		    
