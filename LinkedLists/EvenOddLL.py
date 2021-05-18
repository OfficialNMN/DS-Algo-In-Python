# To segregate even and odd nodes [resent in a linkedlist

def even_odd_segregate(head):
	evenstart=None
	evenend=None
	oddstart=None
	oddend=None
	current=head

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
	head=evenstart
