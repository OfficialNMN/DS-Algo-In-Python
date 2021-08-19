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

# The digits are stored in reverse order, and each of their nodes contains a single digit.
# Add the two numbers and return the sum as a linked list

def addTwoNumbers(l1, l2):
	# creating a dummy node
    dummy=temp=ListNode()
    carry=0
    # iterate till all of these become None
    while(l1!=None or l2!=None or carry):
    	# storing sum of 2 digits
        summ=0
        if l1!=None:
            summ+=l1.val
            l1=l1.next
        if l2!=None:
            summ+=l2.val
            l2=l2.next
        
        summ+=carry
        # updated carry if present
        carry=summ//10
        # creating newnode having data as (sum of digits)%10
        node=ListNode(summ%10)
        # linking of newnode in the list
        temp.next=node
        temp=temp.next
    return dummy.next