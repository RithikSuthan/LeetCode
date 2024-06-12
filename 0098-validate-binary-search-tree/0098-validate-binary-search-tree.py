# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        isCheck=True
        val=float("-inf")
        def validTree(root):
            nonlocal isCheck,val
            if root is None:
                return
            validTree(root.left)
            if val<root.val:
                val=root.val
            else:
                isCheck=False
            validTree(root.right)
        validTree(root)
        if isCheck:
            return True
        return False
        