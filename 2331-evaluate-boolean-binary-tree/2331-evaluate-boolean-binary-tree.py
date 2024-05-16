# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def conversion(self,root):
        if root is None:
            return None
        root.left=self.conversion(root.left)
        root.right=self.conversion(root.right)
        if root.val==0:
            root.val=False
        elif root.val==1:
            root.val=True
        elif root.val==3:
            root.val="and"
        else:
            root.val="or"
        return root
    def postOrder(self,root):
        if root is None:
            return None
        root.left=self.postOrder(root.left)
        root.right=self.postOrder(root.right)
        if root and root.left and root.right and root.left:
            if root.val=="and":
                root.val=root.left.val and root.right.val
            else:
                root.val=root.left.val or root.right.val
        return root
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        val=self.conversion(root)
        val1=self.postOrder(root)
        print(val1)
        return val1.val