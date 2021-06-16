class TreeNode:
	def __init__(self,data):
		self.data=data
		self.left=None
		self.right=None

def LeftView(root):
	if root is None:
	    return  
	# arr to store left nodes
	arr=[]
	# empty queue for level order traversal
	queue = []
	queue.append(root)
	while(len(queue)):
		n=len(queue)
		arr.append(queue[0].data)
		while(n>0):
			n-=1
			node=queue.pop(0)
			if (node.left is not None):
				queue.append(node.left)
			if (node.right is not None):
				queue.append(node.right)
	return arr
				
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
print(LeftView(root))