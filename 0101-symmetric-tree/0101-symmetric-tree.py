# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sym(self,root1,root2):
        if not root1 and not root2:
            return True
        if root1 and root2 is None:
            return False
        if root1 is None and root2:
            return False
        if root1.val!=root2.val:
            return False
        if self.sym(root1.left,root2.right) and  self.sym(root1.right,root2.left):
            return True 
        
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        if self.sym(root.left,root.right):
            return True
        return False