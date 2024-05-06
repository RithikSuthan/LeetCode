# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    blue=0
    def preOrderTraversal(self,root,max1):
        if root is None:
            return 
        if max1<=root.val:
            self.blue=self.blue+1
            max1=max(max1,root.val)
        self.preOrderTraversal(root.left,max1)
        self.preOrderTraversal(root.right,max1)
    def goodNodes(self, root: TreeNode) -> int:
        self.preOrderTraversal(root,float("-inf"))

        print(self.blue)
        return self.blue