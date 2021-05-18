# To remove loop present in a linkedlist

def removeloop(head,loop_node):
	ptr1=head
	while (1):
		ptr2=loop_node
		# start ptr2 untill either it completes the loop or encounters ptr1 in its path
		while (ptr2.next!=loop_node and ptr2.next!=ptr1):
			ptr2=ptr2.next
		# if ptr2 reaches ptr1 then there is loop so break it
		if ptr2.next==ptr1:
			break
		# increase ptr1 till either of while condition satisfied
		ptr1=ptr1.next
	# disconnect ptr2 and ptr1 by making its next null
	ptr2.next=None