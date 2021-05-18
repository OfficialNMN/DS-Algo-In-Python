class Node:
	def __init__(self,data):
		self.data=data
		self.next=None

class LinkedList:
	def __init__(self):
		self.head=None 

	def insert_at_start(self,data):
		newnode=Node(data)
		# making the next of newnode as head
		newnode.next=self.head
		# move the head pointer to new node
		self.head=newnode

	def insert_after_node(self,prev_node,data):
		if not prev_node:
			print('No previous node')
			return
		newnode=Node(data)
		# making next of newnode as next of prevnode
		newnode.next=prev_node.next
		# making next of prevnode as newnode
		prev_node.next=newnode

	def insert_at_last(self,data):
		newnode=Node(data)
		if self.head is None:
			self.head=newnode
			return
		else:
			last=self.head
			# traversing till last node
			while last.next:
				last=last.next
			# making next of last to newnode
			last.next=newnode

l=LinkedList()
l1=LinkedList()

l.insert_at_start(1)
l.insert_at_last(2)
l.insert_at_last(3)
l.insert_at_last(4)
l.insert_at_last(5)
l.insert_at_last(6)

# l.insert_after_node(l.head,2)
