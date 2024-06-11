# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def same(p,q):
            nonlocal same
            if p is None and q is None:
                return True
            if p is None or q is None:
                return False
            elif p.val!=q.val:
                return False 
            return same(p.left,q.left) and same(p.right,q.right)
        return same(p,q)