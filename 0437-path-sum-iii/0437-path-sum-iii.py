# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        ans=0
        def inorder(root,sum1):
            nonlocal ans
            if root is None:
                return 
            sum1+=root.val
            if sum1==targetSum:
                ans+=1
            inorder(root.left,sum1)
            inorder(root.right,sum1)
        def preorder(root):
            if root is None:
                return 
            inorder(root,0)
            preorder(root.left)
            preorder(root.right)
        preorder(root)
        return ans
        