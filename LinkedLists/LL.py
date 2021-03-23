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
			print(current.data)
			current=current.next

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

	def delete(self,location):
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
		

	def search(self,value):
		node=self.head
		while node is not None:
			if node.data==value:
				return 'Found'
			node=node.next
		return -1

	def reverse(self):
		if (self.head==None) or (self.head.next==None):
			return self.head 
		prev=None
		current=self.head
		forward=None
		while (current is not None) :
			# backup pointer so that list is not lost
			forward=current.next   
			# making links reverse
			current.next=prev
			# move forward for same tasks
			prev=current
			current=forward
		# making prev as new head
		self.head=prev

	def detectloop(self):
		s=set()
		temp=self.head
		while(temp):
			if temp in s:
				return True
			s.add(temp)
			temp=temp.next
		return False
	
	def midpoint(self):
		fast=self.head
		slow=self.head
		while(fast.next!=None and fast.next.next!=None):
			slow=slow.next
			fast=fast.next.next
		return slow.data

	def palindrome_util(self,string):
		return (string==string[::-1])

	def isPalindrome(self):
		# creating an array to store elements and then use that array to form a string which can be further compared with its reverse to check palindrome
		current=self.head
		arr=[]
		while current:
			arr.append(str(current.data))
			current=current.next
		string="".join(arr)
		return self.palindrome_util(string)


l=LinkedList()
l.insert_at_start('bc')
l.insert_at_last('dcb')
l.insert_after_node(l.head,'d')
l.insert_at_last('a')
l.insert_at_start('a')
# l.delete(3)
l.traverse()
# l.head.next.next.next.next = l.head       # creating a loop to check 
# print(l.detectloop())                     # detect loop
# print(l.search(4))			    # searching 
# l.reverse()				    # reversing
# l.traverse()							
# print(f'mid : {l.midpoint()}')            # getting midpoint
print(l.isPalindrome())			    # checking palindrome





