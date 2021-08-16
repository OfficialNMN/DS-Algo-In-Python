def sortedMerge(head1, head2):
    # if any list is None
    if head1 == None:
        return head2
    if head2 == None:
        return head1
    
    # creating dummy and current node
    current=dummy=Node(0)
    # next of current will be the smaller of the 2 lists
    while head1 and head2:
        if head1.data<=head2.data:
            current.next=head1
            head1=head1.next
        else:
            current.next=head2
            head2=head2.next
        current=current.next
    
    # to iterate the leftover list    
    if head1:
        current.next=head1
    if head2:
        current.next=head2
    # new head is the next of dummy
    return dummy.next