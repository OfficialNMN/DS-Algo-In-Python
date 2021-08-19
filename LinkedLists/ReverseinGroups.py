
def reverseKGroup(head, k):
    if (head is None or k==1):
        return head
    # creating a dummy node
    dummy=Node(0)
    dummy.next=head
    curr=dummy
    forward=dummy
    prev=dummy
    
    # calculating length of LL
    count=0
    while(curr.next!=None):
        count+=1
        curr=curr.next

    # reversing in k-groups
    while(count>=k):
        curr=prev.next
        forward=curr.next
        for i in range(1,k):
            curr.next=forward.next
            forward.next=prev.next
            prev.next=forward
            forward=curr.next
        prev=curr
        count-=k
    # new head is dummy.next
    return dummy.next
