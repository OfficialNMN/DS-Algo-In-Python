class TreeNode:
	def __init__(self,data):
		self.data=data
		self.left=None
		self.right=None

def input_tree():
	rootdata=int(input())
	if rootdata==-1:
		return None
	root=TreeNode(rootdata)
	# recursive to take input of left tree
	leftTree=input_tree()
	# recursive to take input of right tree
	rightTree=input_tree()
	root.left=leftTree
	root.right=rightTree
	return root

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

