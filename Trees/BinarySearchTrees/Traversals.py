class BST:
	def __init__(self,data):
		self.data=data
		self.left=None
		self.right=None

# Insertion of node
def insertnode(root,value):
	if root.data==None:
		root.data=value
	elif value<=root.data:
		if root.left is None:
			root.left=BST(value)
		else:
			insertnode(root.left,value)
	else:
		if root.right is None:
			root.right=BST(value)
		else:
			insertnode(root.right,value)
	return 'Inserted'

# Deletion of node
def deletenode(root, key):
    if root is None:
        return root
    # if root is not None
    if key < root.data:
        root.left = deletenode(root.left, key)
    elif(key > root.data):
        root.right = deletenode(root.right, key)
    # if key is same as root's key, then this is the node to be deleted
    else:
    	# node with no child or 1 child
        if root.left is None:
            temp = root.right
            root = None
            return temp
 
        elif root.right is None:
            temp = root.left
            root = None
            return temp
        # node with 2 children, then replace it by the inorder successor
        temp = minValue(root.right)
        # copying the data of inorder successor to root
        root.data = temp.data
		# delete the inorder successor
        root.right = deletenode(root.right, temp.data)
 
    return root

# To find minimum of the BST
def minValue(root):
	if root is None:
		return 
	node=root
	while(node.left):
		node=node.left
	return node

# PreOrder Traversal (SLR)
def preorder(root):
	if not root:
		return 
	print(root.data)
	preorder(root.left)
	preorder(root.right)

# InOrder Traversal (LSR)
def inorder(root):
	if not root:
		return 	
	inorder(root.left)
	print(root.data)
	inorder(root.right)

# PostOrder Traversal (LRS)
def postorder(root):
	if not root:
		return 	
	postorder(root.left)	
	postorder(root.right)
	print(root.data)

# Level Order Traversal 
def levelorder(root):
    if not root:
        return
    else:
    	queue = []
    	queue.append(root) 
    	while(len(queue) > 0):
    		node=queue.pop(0)
    		print(node.data)
    		if node.left is not None:
    			queue.append(node.left)
    		if node.right is not None:
    			queue.append(node.right)

# Deletion of Tree
def deleteBST(root):
	root.data=None
	root.right=None
	root.left=None
	return 'Deleted Tree'


newBST=BST(10)
insertnode(newBST,70)
insertnode(newBST,50)
insertnode(newBST,90)
insertnode(newBST,30)
insertnode(newBST,60)
insertnode(newBST,80)
insertnode(newBST,100)
insertnode(newBST,20)
insertnode(newBST,40)
insertnode(newBST,60)

