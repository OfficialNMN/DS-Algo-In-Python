class Solution:
    def reverse(self,head, k):
        if head is None:
            return
        prev=None
        forward=None
        current=head
        count=0
        # reverse once
        while(current is not None and count<k):
            forward=current.next
            current.next=prev
            prev=current
            current=forward
            count+=1
        # now recursively call for left list
        if forward is not None:
            head.next=self.reverse(forward,k)
        return prev
