def rotate(head,k):
    if head is None:
        return 
    # to calculate size
    temp=head
    size=1
    while temp.nxt!=None:
        temp=temp.nxt
        size+=1
    if k>size:
        k=k%size
    k=size-k
    if (k==0 or k==size):
        return head
    
    current=head
    count=1
    while(count<k and current is not None):
        current=current.nxt
        count+=1
    kthnode=current
    temp.nxt=head
    head=kthnode.nxt
    kthnode.nxt=None
    return head