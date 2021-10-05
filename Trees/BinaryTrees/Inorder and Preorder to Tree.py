# To construct a tree from given inorder and preorder traversal

def buildtree(inorder, preorder, n):
    mapper={}
    for i,v in enumerate(inorder):
        mapper[v]=i
    def build(low,high):
        if low>high:
            return
        root=Node(preorder.pop(0))
        mid=mapper[root.data]
        root.left=build(low,mid-1)
        root.right=build(mid+1,high)
        return root
    return build(0,n-1)


# Method using recursion
def buildtree(inorder, preorder, n):
    return build(inorder,preorder)

def build(inorder,preorder):
    if not inorder:
        return
    root=Node(preorder.pop(0))
    mid=inorder.index(root.data)
    root.left=build(inorder[:mid],preorder)
    root.right=build(inorder[mid+1:],preorder)
    return root