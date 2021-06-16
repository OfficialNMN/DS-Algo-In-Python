class TreeNode:
	def __init__(self,data):
		self.data=data
		self.left=None
		self.right=None

	def height(self,root):
		if root==None:
			return 0    
		lh=self.height(root.left)
		rh=self.height(root.right)
		return max(lh,rh)+1

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

print(root.height(root))