# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    valid=True
    prev=float("-inf")
    def inorder(self,root):
        if root is None:
            return
        self.inorder(root.left)
        if self.prev<root.val:
            self.prev=root.val
        else:
            self.valid=False
        self.inorder(root.right)
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.inorder(root)
        return self.valid