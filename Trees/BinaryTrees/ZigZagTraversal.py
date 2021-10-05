#Function to store the zig zag order traversal of tree in a list.
def zigZagTraversal(root):
    result=[]
    def dfs(node,level,result):
        if node is None:
            return 
        if len(result)<=level:
            result+=[[]]
        dfs(node.left,level+1,result)
        dfs(node.right,level+1,result)
        if level%2==0:
            result[level].append(node.data)
        else:
            result[level].insert(0,node.data)
    dfs(root,0,result)
    return result