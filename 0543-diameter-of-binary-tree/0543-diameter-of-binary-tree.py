# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        dia=0
        def height(root):
            nonlocal dia
            if root is None:
                return 0
            lheight=height(root.left)
            rheight=height(root.right)
            dia=max(dia,lheight+rheight)
            if lheight>rheight:
                return lheight+1
            return rheight+1
        # print(dia)
        height(root)
        return dia
