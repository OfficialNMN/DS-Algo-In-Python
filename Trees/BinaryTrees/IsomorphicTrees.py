class TreeNode:
	def __init__(self,data):
		self.data=data
		self.left=None
		self.right=None

def isIsomorphic(self, root1, root2): 
	if root1 is None and root2 is None:
		return True
	if root1 is None or root2 is None:
		return False
	if root1.data != root2.data:
		return False
	# checking left of 2 trees and right of 2 trees
	return ((self.isIsomorphic(root1.left,root2.left) and 
		self.isIsomorphic(root1.right,root2.right)) 
	or  # check right with left of other tree and vice-versa
		(self.isIsomorphic(root1.left,root2.right) and 
		self.isIsomorphic(root1.right,root2.left)))

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)