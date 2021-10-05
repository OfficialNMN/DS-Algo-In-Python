# iterative pre-order traversal using stack
def preorderTraversal(root):
    pre=[]
    if root is None:
        return pre
    stack=[]
    stack.append(root)
    while(stack):
        r=stack.pop()
        pre.append(r.val)
        if r.right is not None:
            stack.append(r.right)
        if r.left is not None:
            stack.append(r.left)
    return pre

# iterative inorder traversal