# Clone a linkedlist with random and next pointer

def clone(head):
	# insert new node after every node of original list
	curr=head
	while curr:
		new=Node(curr.data)
		new.next=curr.next
		curr.next=new
		curr=curr.next

	# adjust the random pointers of new node
	curr=head
	while curr:
		if curr.random:
			curr.next.random=curr.random.next
		curr=curr.next.next

	# detach original and duplicate lists from each other
	curr=head
	duplicate_head=head.next
	while curr.next!=None:
		temp=curr.next
		curr.next=curr.next.next
		curr=temp

	# duplicate head will be the head of cloned list
	return duplicate_head