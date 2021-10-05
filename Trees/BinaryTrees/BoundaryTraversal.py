class Solution:
    def printBoundaryView(self,root):
        ans=[]
        if self.isleaf(root) is False:
            ans.append(root.data)
        self.left_boundary(root,ans)
        self.leaf_nodes(root,ans)
        self.reverse_right_boundary(root,ans)
        return ans
    
    # to check whether leaf or not
    def isleaf(self,root):
        if root.left is None and root.right is None:
            return True
        return False
    
    # add left boundary first that are not leafs
    def left_boundary(self,root,res):
        curr=root.left
        while curr:
            if self.isleaf(curr) is False:
                res.append(curr.data)
            if curr.left is not None:
                curr=curr.left
            else:
                curr=curr.right
    
    # then add leaves excluding those in right or left boundary
    def leaf_nodes(self,root,res):
        if self.isleaf(root):
            res.append(root.data)
            return
        if root.left is not None:
            self.leaf_nodes(root.left,res)
        if root.right is not None:
            self.leaf_nodes(root.right,res)

    # add right boundary that are nor leafs and then reverse that
    def reverse_right_boundary(self,root,res):
        curr=root.right
        temp=[]
        while curr:
            if self.isleaf(curr) is False:
                temp.append(curr.data)
            if curr.right is not None:
                curr=curr.right
            else:
                curr=curr.left
        for i in range(len(temp)-1,-1,-1):
            res.append(temp[i])