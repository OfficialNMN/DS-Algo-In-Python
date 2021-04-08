class TreeNode:
	def __init__(self,data):
		self.data=data
		self.left=None
		self.right=None

def count_nodes(root):
	if root==None:
		return 0
	left_count=count_nodes(root.left)
	right_count=count_nodes(root.right)
	return 1+left_count+right_count

def height(root):
	if root==None:
		return -1    # -1 for edges,0 for nodes
	lh=height(root.left)
	rh=height(root.right)
	return max(lh,rh)+1

def sum_nodes(root):
	if root==None:
		return 0
	left_sum=sum_nodes(root.left)
	right_sum=sum_nodes(root.right)
	return root.data+left_sum+right_sum

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

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

