# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        def preorder(root):
            if root is None:
                return 
            if root.left:
                if root.left and root.left.right:
                    temp=root.left.right
                    while(temp.right):
                        temp=temp.right
                    aux=root.right
                    root.right=root.left
                    temp.right=aux
                else:
                    temp=root.right
                    root.right=root.left
                    root.right.right=temp
                root.left=None
            preorder(root.left)
            preorder(root.right)
        preorder(root)
        