def rotate(head,k):
    if (head is None or head.next is None or k==0):
        return head
    # calculating length of list
    curr=head
    count=1
    while(curr.next!=None):
        count+=1
        curr=curr.next
    # connecting last node to head
    curr.next=head
    k=k%count
    k=count-k
    while(k>0):
        curr=curr.next
        k-=1
    # making next node of current as head
    head=curr.next
    # current will be the last node
    curr.next=None
    return head