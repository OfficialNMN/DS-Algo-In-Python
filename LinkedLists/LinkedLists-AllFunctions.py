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
		slow=fast=self.head
		while(slow and fast and fast.next):
			slow=slow.next
			fast=fast.next.next
			if slow==fast:
				return True
		return False

	def removeloop(self,loop_node):
		ptr1=self.head
		while (1):
			ptr2=loop_node
			# start from loop_node and check 
			while (ptr2.next!=loop_node and ptr2.next!=ptr1):
				ptr2=ptr2.next
			# if ptr2 reaches ptr1 then there is loop so break it
			if ptr2.next==ptr1:
				break
			ptr1=ptr1.next
		# ptr2 will be the last node so make the next of it null
		ptr2.next=None
	
	def midpoint(self):
		fast=self.head
		slow=self.head
		while(fast.next!=None and fast.next.next!=None):
			slow=slow.next
			fast=fast.next.next
		return slow.data

	def palindrome_util(self,string):
		# comparing the reverse 
		return (string==string[::-1])

	def isPalindrome(self):
		# creating an array to store elements and then use that array to form a string which can be further compared with its reverse to check palindrome
		current=self.head
		arr=[]
		while current is not None:
			arr.append(str(current.data))
			current=current.next
		string="".join(arr)
		return self.palindrome_util(string)

	def RemoveDuplicates(self):
		current=self.head
		if current is None:
			return 
		while current.next is not None:
			if current.data==current.next.data:
				# so that list is not lost after deleting duplicate element
				lost=current.next.next
				# deleting duplicate
				current.next=None
				current.next=lost
			else:
				current=current.next

	def merge2sorted(self,headA,headB):
		# dummy to store result list
		dummy=Node(0)
		# tail to keep track of last element of result list
		tail = dummy
		while(True):
			if headA is None:
				tail.next=headB
				break
			if headB is None:
				tail.next=headA
				break

			if headA.data<=headB.data:
				tail.next=headA
				headA=headA.next
			else:
				tail.next=headB
				headB=headB.next

			# increase the tail
			tail=tail.next
		# return next of dummy as it is starting of merges list
		return dummy.next

	def even_odd_segregate(self):
		evenstart=None
		evenend=None
		oddstart=None
		oddend=None
		current=self.head

		while (current):
			val=current.data
			# if value is even inserting in even list
			if (val%2)==0:
				if (evenstart==None):
					evenstart=current
					evenend=evenstart
				else:
					evenend.next=current
					evenend=evenend.next
			# if value is odd inserting in odd list
			else:
				if (oddstart==None):
					oddstart=current
					oddend=oddstart
				else:
					oddend.next=current
					oddend=oddend.next
			current=current.next

		# if anyone of odd or even list is empty
		if(oddstart==None or evenstart==None):
			return
		# appending the starting of odd to end of even
		evenend.next=oddstart
		oddend.next=None
		# setting head as evenstart
		self.head=evenstart


l=LinkedList()
l1=LinkedList()

l.insert_at_start(1)
l.insert_at_last(2)
l.insert_at_last(3)
l.insert_at_last(4)
l.insert_at_last(5)
l.insert_at_last(6)

# l.insert_after_node(l.head,2)
# deletion
# l.delete('a')

# creating a loop to check 
# l.head.next.next.next.next = l.head    

# detect loop
# print(l.detectloop()) 

# searching 
# print(l.search(4))

# reversing
# l.reverse()								
# l.traverse()	

# getting midpoint						
# print(f'mid : {l.midpoint()}')

# checking palindrome			
# print(l.isPalindrome())

# remove duplicates			    
# l.RemoveDuplicates()

# merging 2 sorted lists                      
# l.head=l.merge2sorted(l.head,l1.head)     

# segregation with even nodes followed by odd nodes
# l.even_odd_segregate()
l.traverse()


