# To merge 2 sorted linkedlists into one single

def merge2sorted(a,b):
	result=None
	# if any of the list becomes null
	if a==None:
		return b
	if b==None:
		return a

	if a.data<=b.data:
		result = a
		result.next=merge2sorted(a.next,b)
	else:
		result = b
		result.next=merge2sorted(a,b.next)

def mid(h):
	if h is None:
		return
	slow=fast=head
	while(fast.next is not None and fast.next.next is not None):
		slow=slow.next
		fast=fast.next.next
	return slow

def mergesort(h):
	if h==None or h.next==None:
		return h
	
	middle=mid(h)
	midnext=mid.next

	left=mergesort(h)
	right=mergesort(midnext)

	sortedlist=merge2sorted(left,right)
	return sortedlist

