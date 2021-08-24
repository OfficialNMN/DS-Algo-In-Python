def reverse(head):
	if (head==None) or (head.next==None):
		return head 
	prev=None
	current=head
	forward=None
	while (current is not None) :
		# backup pointer so that list is not lost
		forward=current.next   
		# making links reverse
		current.next=prev
		# move forward for same tasks
		prev=current
		current=forward
	# prev will be the new head
	return prev
