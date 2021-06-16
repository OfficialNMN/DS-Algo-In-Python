def areMirror(self,root1,root2):
    if root1 is None and root2 is None:
        return 1
    if root1.data!=root2.data:
        return 0
    if root1.data==root2.data:
        return self.areMirror(root1.left,root2.right) and self.areMirror(root1.right,root2.left)