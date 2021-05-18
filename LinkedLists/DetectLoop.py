def detectloop(head):
	slow=fast=head
	while(slow and fast and fast.next):
		slow=slow.next
		fast=fast.next.next
		# if both slow and fast meet we have a loop
		if slow==fast:
			return True
	return False

# creating a loop to check 
l.head.next.next.next.next = l.head    