# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ls=[]
        def post_order(root):
            nonlocal ls
            if root is None:
                return
            post_order(root.left)
            post_order(root.right)
            ls.append(root.val)
        post_order(root)
        return ls