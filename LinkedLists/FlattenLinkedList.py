def merge(a,b):
    # dummy node to create a new List
    temp=Node(0)
    result=temp
    
    # using the concept of merge 2 linkedlists
    while(a!=None and b!=None):
        if(a.data<b.data):
            temp.bottom=a
            temp=temp.bottom
            a=a.bottom
        else:
            temp.bottom=b
            temp=temp.bottom
            b=b.bottom
    
    # if one list gets exhausted then traverse the other
    if (a!=None):
        temp.bottom=a
    else:
        temp.bottom=b
    # result.bottom will the new head of the flattened list
    return result.bottom

def flatten(root):
    if root==None or root.next==None:
        return root
    # move to next node in List
    root.next=flatten(root.next)
    # calling merge recursively
    root=merge(root,root.next)
    return root