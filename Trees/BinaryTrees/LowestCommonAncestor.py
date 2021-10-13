# The LCA or Lowest Common Ancestor as the common ancestor of both the nodes which 
# is closest to them.

class TreeNode:
	def __init__(self,data):
		self.data=data
		self.left=None
		self.right=None

def LCA(root,n1,n2):
	if root is None:
		return
	# If any of the given keys (n1 and n2) matches with the root, then the root is LCA.
	if root.data==n1 or root.data==n2:
		return root.data

	# recursively find in left subtree and right subtree
	left_lca=LCA(root.left,n1,n2)
	right_lca=LCA(root.right,n1,n2)

	# node which has one key present in its left subtree and the other 
	# key present in the right subtree is the LCA
	if left_lca is not None and right_lca is not None:
		return root.data

	# If both keys lie in the left subtree, then the left subtree has LCA , 
	# otherwise, LCA lies in the right subtree.  
	return left_lca if left_lca is not None else right_lca

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

print(LCA(root, 4, 6))