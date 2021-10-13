class TreeNode:
	def __init__(self,data):
		self.data=data
		self.left=None
		self.right=None

def leftSideView(root):
    ans=[]
    level=0
    traverse(root,level,ans)
    return ans

# doing level order traversal and adding the first node at every level
def traverse(node,level,ans):
    if node is None:
        return
    if level==len(ans):
        ans.append(node.data)
    traverse(node.left,level+1,ans)
    traverse(node.right,level+1,ans)
    

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

print(leftSideView(root))