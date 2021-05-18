class Node:
	def __init__(self,data):
		self.data=data
		self.next=None

class LinkedList:
	def __init__(self):
		self.head=None   

	def delete_at_location(self,location):
		# if list is empty
		if self.head is None:
			return 
		temp=self.head
		if location==0:
			self.head=temp.next
			temp=None
			return 
		for i in range(location-1):
			temp=temp.next
			if temp is None:
				break
		# If position is more than number of nodes
		if temp is None:
			return 
		if temp.next is None:
			return
        # store pointer to the next of node to be deleted
		new_next=temp.next.next
		# temp.next is to be unlinked 
		temp.next=None
		temp.next=new_next	

	def delete_data(self,data):
		current = self.head
		previous = None
		while current is not None:
			if current.data == data:
    			# if this is the head node
				if previous is not None:
					previous.next = current.next
				else:
					self.head = current.next
			previous = current
			current = current.next