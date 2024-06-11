# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def sameTree(root,subRoot):
            if root is None and subRoot is None:
                return True
            if root is None or subRoot is  None:
                return False
            elif root.val!=subRoot.val:
                return False
            return sameTree(root.left,subRoot.left) and sameTree(root.right,subRoot.right)
        result=False    
        def tree(root,subRoot):
            nonlocal result
            if root is None:
                return
            tree(root.left,subRoot)
            if (root.val==subRoot.val):
                if sameTree(root,subRoot) and not result:
                    result=True
            tree(root.right,subRoot)
        tree(root,subRoot)
        return result 