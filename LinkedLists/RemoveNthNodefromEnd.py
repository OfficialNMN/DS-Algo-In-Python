# Brute force approach is to iterate to check the length of the linked list
# and the again iterate for (length-n) times and break the link 

# Efficient Approach
def removeNthFromEnd(head,n):
    # creating dummy node and setting it to head         
    start = ListNode()
    start.next=head
    # creating 2 pointers
    slow=start
    fast=start
    # iterating fast n times         
    for i in range(n):
        fast=fast.next
    # moving both slow and fast till fast is at last node         
    while (fast.next!=None):
        fast=fast.next
        slow=slow.next
    # breaking the link from the node to be removed        
    slow.next=slow.next.next
    # new head is start .next
    return start.next