def LCA(root, n1, n2):
    # if n1 and n2 both are greater than root move to right 
    if n1>root.data and n2>root.data:
        return LCA(root.right,n1,n2)
    # if n1 and n2 both less than root move to left
    if n1<root.data and n2<root.data:
        return LCA(root.left,n1,n2)
    # else print root which will be our lca
    else:
        return root