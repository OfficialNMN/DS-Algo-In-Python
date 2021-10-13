class TreeNode:
	def __init__(self,data):
		self.data=data
		self.left=None
		self.right=None
		
# To print node a K distance from root
def printKDistant(root, k):
    if root is None or k<0:
        return 
    # if k is achieved
    if k == 0:
        print(root.data)
    # otherwise look in left and right subtrees
    else:
        printKDistant(root.left, k-1)
        printKDistant(root.right, k-1)

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

# To print all nodes at a K distance form the target node
    
def KDistanceNodes(root,target,k):
    if root is None:
        return -1
    # if target node is root then apply KDown method
    if root==target:
        KDistanceDown(root,k)
        return 
    # search in left subtree
    left_d=KDistanceNodes(root.left,target,k)
    # if found in left
    if left_d!=-1:
        # if found at k distance
        if left_d+1==k:
            print(root.data)
        # else go to right subtree k-2-left_d
        else:
            KDistanceDown(root.right,k-2-left_d)
        return 1+left_d
    # search in right subtree
    right_d=KDistanceNodes(root.right,target,k)
    # if found in right
    if right_d!=-1:
        # if found at k distance
        if right_d+1==k:
            print(root.data)
        # else go to left subtree at k-2-right_d
        else:
            KDistanceDown(root.left,k-2-right_d)
        return 1+right_d
    return -1
            

def KDistanceDown(root,k):
    if root is None or k<0:
        return 
    if k==0:
        print(root.data)
        return
    KDistanceDown(root.left,k-1)
    KDistanceDown(root.right,k-1)