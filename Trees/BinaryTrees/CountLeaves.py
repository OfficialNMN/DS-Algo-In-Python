class TreeNode:
	def __init__(self,data):
		self.data=data
		self.left=None
		self.right=None
		
def count_nodes(root):
	if root==None:
		return 0
	left_count=count_nodes(root.left)
	right_count=count_nodes(root.right)
	return 1+left_count+right_count

def countleaves(root):
	if root is None:
		return 0
	if root.left==None and root.right==None:
		return 1
	return countleaves(root.left)+countleaves(root.right)

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
