def add2Lists(first,second):
	# converting both lists into strings
	n1,n2="",""
	while first:
		n1=n1+str(first.data)
		first=first.next
	while second:
		n2=n2+str(second.data)
		second=second.next
	# if any string is emty the make it "0"
	if not n1: n1="0"
	if not n2: n2="0"
	# converting strings to int and then added
	summed=int(n1)+int(n2)
	# creating a new current node, newhead for a new linked list with data=0
	curr = Node(0)
	newhead=curr
	# lopping in summed string
	for i in str(summed):
		# making next of curr as node with integer in summed string
		curr.next=Node(int(i))
		# iterating ahead to add other nodes
		curr=curr.next
	return newhead.next
