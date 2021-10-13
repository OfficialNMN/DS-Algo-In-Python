# helper function to calculate sum of every subtree
def sumtree(node):
    if node is None:
        return 0
    return node.data+sumtree(node.left)+sumtree(node.right)

def isSumTree(root):
    # leaf node case
    if root is None or (root.left is None and root.right is None):
        return 1
    leftsum=sumtree(root.left)
    rightsum=sumtree(root.right)
    c=root.data
    # to check whether sum tree or not
    if root.data==leftsum+rightsum and isSumTree(root.left) and isSumTree(root.right):
        return 1
    return 0