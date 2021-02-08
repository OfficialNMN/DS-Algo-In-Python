# Using LinkedLists

class TreeNode:
	def __init__(self,data):
		self.data=data
		self.leftchild=None
		self.rightchild=None

Btree=TreeNode("Drinks")
leftchild=TreeNode("Hot")
rightchild=TreeNode("Cold")
Btree.leftchild=leftchild
Btree.rightchild=rightchild

# PreOrder Traversal
def preorder(rootnode):
	if not rootnode:
		return 
	print(rootnode.data)
	preorder(rootnode.leftchild)
	preorder(rootnode.rightchild)

preorder(Btree)
