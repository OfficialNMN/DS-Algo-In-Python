def midpoint(head):
	# slow and fast 2 pointers
	fast=head
	slow=head
	while(fast.next!=None and fast.next.next!=None):
		slow=slow.next
		# fast moves double the speed of slow
		fast=fast.next.next
	# when fast one gets exhausted then slow will be the mid
	return slow.data

print(f'mid : {l.midpoint()}')