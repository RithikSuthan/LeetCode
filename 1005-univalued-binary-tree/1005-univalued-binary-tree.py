# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        flag=True
        val=root.val
        def inorder(root):
            nonlocal flag
            if root is None:
                return
            if(val!=root.val):
                flag=False 
            inorder(root.left)
            inorder(root.right)
        inorder(root)
        return flag