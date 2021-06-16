class TreeNode:
	def __init__(self,data):
		self.data=data
		self.left=None
		self.right=None

def leftcloned(root):
	if root is None:
		return
	# recursively calling cloned for left and right subtree
	lcl=leftcloned(root.left)
	lcr=leftcloned(root.right)
	# creating new left to attach to left of root while right to root will be same 
	newleft=TreeNode(root.data)
	# left of newnode will be the lcl and right will be null
	newleft.left=lcl
	root.left=newleft
	root.right=lcr
	return root

# to transform ack to normal binary tree from a left cloned tree
def transformback(root):
	if root is None:
		return
	lnn=transformback(root.left.left)
	rnn=transformback(root.right)
	root.left=lnn
	root.right=rnn
	return root

def printPostorder(root):
    if root:
        printPostorder(root.left)
        printPostorder(root.right)
        print(root.data)

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

leftcloned(root)
printPostorder(root)
print('after transformback')
transformback(root)
printPostorder(root)