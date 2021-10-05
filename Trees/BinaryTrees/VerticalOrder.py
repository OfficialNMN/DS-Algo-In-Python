class TreeNode:
	def __init__(self,data):
		self.data=data
		self.left=None
		self.right=None

def width(root,hl,ans):
	# hl-horizontal level
	if root is None:
		return 
	# creating an array to store left hl and right hl
	ans[0]=min(ans[0],hl)
	ans[1]=max(ans[1],hl)
	# going to left hl=hl-1
	width(root.left,hl-1,ans)
	# going to right hl=hl+1 
	width(root.right,hl+1,ans)
	return ans[1]-ans[0]+1

def verticalorderhelper(root,hl,m):
	if root is None:
		return
	else:
		if hl in m:
			m[hl].append(root.data)
		else:
			m[hl]=[root.data]
	verticalorderhelper(root.left,hl-1,m)
	verticalorderhelper(root.right,hl+1,m)

def verticalorder(root):
	m={}
	hl=0
	ans=[]
	verticalorderhelper(root,hl,m)
	for index,value in enumerate(sorted(m)):
		for j in m[value]:
			print(j,end=' ')
		print()


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)
root.right.left.right = TreeNode(8)
root.right.right.right = TreeNode(9)

verticalorder(root)
