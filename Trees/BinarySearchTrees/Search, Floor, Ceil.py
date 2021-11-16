# Time Complexity - O(logn)
def searchBST(root,val):
    while (root is not None and root.data!=val):
        # applying binary search technique
        if root.data>val:
            root=root.left
        else:
            root=root.right
    return root


# To find ceil of the given value in a BST
# Time Complexity - O(logn)
def ceilBST(root,val):
    if root.data==val:
        return root.data
    elif root.data>val:
        val=root.data
        root=root.left
    else:
        root.root.right

# To find floor of the given value in a BST
# Time Complexity - O(logn)
def floorBST(root,val):
    if root.data==val:
        return root.data
    elif root.data<val:
        val=root.data
        root=root.right
    else:
        root.root.left