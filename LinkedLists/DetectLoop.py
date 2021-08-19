def hasCycle(head):
    if head is None or head.next is None:
        return None
    slow=head
    fast=head
    # both fast and slow will meet if theres a list present
    while(fast.next!=None and fast.next.next!=None ):
        slow=slow.next
        fast=fast.next.next
        if fast==slow:
            return True
    return False

# creating a loop to check 
l.head.next.next.next.next = l.head    

# Find starting point of Loop 
# Using Floyd Cycle Detection Algorithm

def detectCycleStart(head):
    if head==None or head.next==None:
        return None
    slow=head
    fast=head
    entry=head
    # to detect whether cycle is there or not
    while(fast.next!=None and fast.next.next!=None):
        slow=slow.next
        fast=fast.next.next
        if slow==fast:
            # this means a cycle exist
            # now we traverse both slow and entry to find the cycle point
            while(slow!=entry):
                slow=slow.next
                entry=entry.next
            # point where entry and slow collides is our answer
            return entry
    # no cycle present
    return None

