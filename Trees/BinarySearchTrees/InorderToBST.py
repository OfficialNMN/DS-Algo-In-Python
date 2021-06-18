class BST:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

def buildTree (inorder, start, end):
    if start > end:
        return None 
    mid=(start+end)//2
    root = BST(inorder[mid]) 
    root.left = buildTree (inorder, start, mid - 1) 
    root.right = buildTree (inorder, mid + 1, end) 
  
    return root

r=buildTree(inorder,0,len(inorder)-1)
