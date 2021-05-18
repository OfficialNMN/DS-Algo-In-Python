# Intersection of 2 Y shaped LinkedLists

def intersetPoint(head1,head2):
    # to get size of both lists
    t1,t2=head1,head2
    len1=0
    while t1:
        len1+=1
        t1=t1.next
    len2=0
    while t2:
        len2+=1
        t2=t2.next
    
    # whichever is longer will be traversed till diff length
    if len1>len2:
        diff=(len1-len2)
        long=head1
        short=head2
    else:
        diff=(len2-len1)
        long=head2
        short=head1
    
    i=0    
    while(i<diff):
        long=long.next
        i+=1
    
    # when both are of same length then both are traversed simultaneously
    while(long!=short):
        long=long.next
        short=short.next
    return long.data