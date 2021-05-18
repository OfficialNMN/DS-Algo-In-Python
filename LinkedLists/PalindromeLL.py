# Tocheck whether linkedlist is palindrome or not

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
