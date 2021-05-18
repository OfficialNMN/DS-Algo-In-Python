class TreeNode:
	def __init__(self,data):
		self.data=data
		self.left=None
		self.right=None

# To find path of root node to given node
def nodeToroot(node,data):
	# if node is none then return False
	if node==None:
		return False
	# check from root node
	# wherever condition is true append that node to path array
	if node.data==data:
		path.append(node.data)
		return True
	# check in left subtree
	find_left=nodeToroot(node.left,data)
	if find_left is True:
		path.append(node.data)
		return True
	# check in right subtree
	find_right=nodeToroot(node.right,data)
	if find_right is True:
		path.append(node.data)
		return True

	# if not found anywhere
	return False

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

print(nodeToroot(root,2))
