class TreeNode:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

def topView(root):
    if root is None:
        return
    ans=[]
    m={}
    q=[]
    q.append([root,0])
    while q:
        c=q.pop(0)
        node=c[0]
        vl=c[1]   # vertical level
        # insert only if vl doesnot alreadyexist in the map
        if vl not in m:
            m[vl]=[node.data]
        if node.left is not None:
            q.append([node.left,vl-1])
        if node.right is not None:
            q.append([node.right,vl+1])
    for i in sorted(m.keys()):
        ans.append(m[i][0])
    return ans

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)
root.right.left.right = TreeNode(8)
root.right.right.right = TreeNode(9)

print(topView(root))