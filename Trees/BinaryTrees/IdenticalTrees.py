# To check whether 2 trees are identical or not
def isIdentical(root1, root2):
    if root1 is None or root2 is None:
        return root1==root2
    return (root1.data==root2.data) and 
    isIdentical(root1.left,root2.left) and 
    isIdentical(root1.right,root2.right)



# To check 2 trees are Mirror/ Symmetric Trees or not
def isSymmetric(root):
    if root is None:
        return
    else:
        return helper(root.left,root.right)

def helper(left,right):
    if right is None or left is None:
        return right==left
    if right.val!=left.val:
        return False
    # checking symmetry in subtree
    return helper(left.left,right.right) and helper(left.right,right.left)