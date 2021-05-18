# To merge 2 sorted linkedlists into one single

def merge2sorted(headA,headB):
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

l.head=l.merge2sorted(l.head,l1.head) 