class TreeNode:
	def __init__(self,data):
		self.data=data
		self.left=None
		self.right=None
		
# To print node a K distance from root
def printKDistant(root, k):
    if root is None or k<0:
        return 
    # if k is achieved
    if k == 0:
        print(root.data)
    # otherwise look in left and right subtrees
    else:
        printKDistant(root.left, k-1)
        printKDistant(root.right, k-1)

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)