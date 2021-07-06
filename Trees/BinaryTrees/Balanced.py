def isBalanced(root):
    if balance(root)!=-1:
        return True
    else:
        return False

# will return the balanced value if in range otherwise -1
def balance(root):
    if root is None:
        return 0
    # recursively check for left
    lh=balance(root.left)
    if lh==-1:
        return -1
    # recursively check for right
    rh=balance(root.right)
    if rh==-1:
        return -1
    # will start from the leftmost node and continue till root
    if abs(lh-rh)>1:
        # wherever rule is violated -1 is returned
        return -1
    else:
        # else height will be returned till that node
        return max(lh,rh)+1