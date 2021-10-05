class TreeNode:
	def __init__(self,data):
		self.data=data
		self.left=None
		self.right=None

def printInorder(root): 
    if root:
        printInorder(root.left)
        print(root.data)
        printInorder(root.right)
 
def printPostorder(root):
    if root:
        printPostorder(root.left)
        printPostorder(root.right)
        print(root.data)
 
def printPreorder(root):
    if root:
        print(root.data)
        printPreorder(root.left)
        printPreorder(root.right)

def printLevelOrder(root):
    if root is None:
        return  
    # empty queue for level order traversal
    queue = []
    queue.append(root)
 
    while(len(queue) > 0):
        print(queue[0].data)
        node = queue.pop(0)
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

# recursive 
def postOrder(root):
    if root is None:
        return []
    return postOrder(root.left)+postOrder(root.right)+[root.data]