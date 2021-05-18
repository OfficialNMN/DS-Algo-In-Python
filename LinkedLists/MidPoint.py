# fast and slow pointer approach

def midpoint(head):
	fast=head
	slow=head
	while(fast.next!=None and fast.next.next!=None):
		slow=slow.next
		fast=fast.next.next
	return slow.data

print(f'mid : {l.midpoint()}')