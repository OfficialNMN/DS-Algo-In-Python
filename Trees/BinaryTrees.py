class TreeNode:
	def __init__(self,data):
		self.data=data
		self.left=None
		self.right=None

def input_tree():
	rootdata=int(input())
	if rootdata==-1:
		return None
	root=TreeNode(rootdata)
	# recursive to take input of left tree
	leftTree=input_tree()
	# recursive to take input of right tree
	rightTree=input_tree()
	root.left=leftTree
	root.right=rightTree
	return root

def count_nodes(root):
	if root==None:
		return 0
	left_count=count_nodes(root.left)
	right_count=count_nodes(root.right)
	return 1+left_count+right_count

def height(root):
	if root==None:
		return 0    
	lh=height(root.left)
	rh=height(root.right)
	return max(lh,rh)+1

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

# To print node a K distance from root
def printKDistant(root, k):
    if root is None or k<0:
        return 
    if k == 0:
        print(root.data)
    else:
        printKDistant(root.left, k-1)
        printKDistant(root.right, k-1)

def countleaves(root):
	if root is None:
		return 0
	if root.left==None and root.right==None:
		return 1
	return countleaves(root.left)+countleaves(root.right)

# Diameter of a binary tree is the longest distance b/w any two nodes
def diameter(root):
	if root is None:
		return 0
	# case-1 When diameter is leftheight + rightheight
	lheight=height(root.left)
	rheight=height(root.right)

	# case-2 when diameter lies on left side only
	ldiameter=diameter(root.left)

	# case-3 when diameter lies on right side only
	rdiameter=diameter(root.right)

	# we have to retrun the max of these 3 cases
	return max(lheight+rheight+1,max(ldiameter,rdiameter)) 

# The LCA or Lowest Common Ancestor as the common ancestor of both the nodes which is closest to them.
def LowestCommonAncestor(node1,node2):
	path1=nodeToroot(root,node1)
	path2=nodeToroot(root,node2)
	for i in range(len(path1)):
		if path1[i]!=path2[i]:
			return path1[i-1]
			break

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

# To get path from given node to root
# print(nodeToroot(root,2))

# Views of Tree
# RightView(root)

# print(LowestCommonAncestor(4,5))
