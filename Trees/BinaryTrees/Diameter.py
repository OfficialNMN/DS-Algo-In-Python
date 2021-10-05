class TreeNode:
	def __init__(self,data):
		self.data=data
		self.left=None
		self.right=None

def diameterOfBinaryTree(root):
    diameter=[0]
    height(root,diameter)
    return diameter[0]
    

def height(root,diameter):
    if root is None:
        return 0
    lh=height(root.left,diameter)
    rh=height(root.right,diameter)
    diameter[0]=max(diameter[0],lh+rh)
    return 1+max(lh,rh)

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

print(diameter(root))