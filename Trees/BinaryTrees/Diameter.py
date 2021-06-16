class TreeNode:
	def __init__(self,data):
		self.data=data
		self.left=None
		self.right=None

def height(root):
	if root==None:
		return 0    
	lh=height(root.left)
	rh=height(root.right)
	return max(lh,rh)+1


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

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

print(diameter(root))