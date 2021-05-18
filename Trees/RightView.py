class TreeNode:
	def __init__(self,data):
		self.data=data
		self.left=None
		self.right=None

def RightView(root):
	if root is None:
	    return  
	# empty queue for level order traversal
	queue = []
	queue.append(root)
	while(len(queue) > 0):
		size=len(queue)
		# Traversing the current level of tree
		for i in range(1,size+1):
			# printing the rightmost element of queue
			node = queue.pop(0)
			if i==size:
				print(node.data)
        	#Enqueue left child
			if node.left is not None:
				queue.append(node.left)
        	# Enqueue right child
			if node.right is not None:
				queue.append(node.right)
				
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
RightView(root)