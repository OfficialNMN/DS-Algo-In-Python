# To remove all duplicates present in a linkedlist

def RemoveDuplicates(head):
	current=head
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
