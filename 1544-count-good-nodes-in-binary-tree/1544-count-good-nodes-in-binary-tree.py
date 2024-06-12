# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        cou=0
        max_val=[]
        def preOrder(root):
            nonlocal cou,max_val
            if root is None:
                return
            max_val.append(root.val)
            if root.val>=max(max_val):
                cou=cou+1
            preOrder(root.left)
            preOrder(root.right)
            max_val.pop()
        preOrder(root)
        return cou