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

# PreOrder Traversal (SLR)
def preorder(rootnode):
	if not rootnode:
		return 
	print(rootnode.data)
	preorder(rootnode.leftchild)
	preorder(rootnode.rightchild)

preorder(Btree)

# InOrder Traversal (LSR)
def inorder(rootnode):
	if not rootnode:
		return 	
	preorder(rootnode.leftchild)
	print(rootnode.data)
	preorder(rootnode.rightchild)

inorder(Btree)

# PostOrder Traversal (LRS)
def postorder(rootnode):
	if not rootnode:
		return 	
	preorder(rootnode.leftchild)	
	preorder(rootnode.rightchild)
	print(rootnode.data)

postorder(Btree)
