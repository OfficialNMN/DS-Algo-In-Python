# To check whether linkedlist is palindrome or not

def palindrome_util(string):
	# comparing the reverse 
	return (string==string[::-1])

def isPalindrome(head):
	# creating an array to store elements and then use that array to form a string which can be further compared with its reverse to check palindrome
	current=head
	arr=[]
	while current is not None:
		arr.append(str(current.data))
		current=current.next
	string="".join(arr)
	return palindrome_util(string)

# Space Efficient Approach

def palindromeLL(head):
	if (head is None or head.next is None):
		return True

	slow=head
	fast=head
	# find middle of LL
	while(fast.next!=None and fast.next.next!=None):
		slow=slow.next
		fast=fast.next.next

	# reverse the right half of LL
	slow.next=reverse(slow.next)
	# move slow to right half 1st node
	slow=slow.next

	# compare values in both halves
	while(slow!=None):
		if (head.data!=slow.data):
			return False
		head=head.next
		slow=slow.next
	return True

# since the above list modifies the original LL
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



