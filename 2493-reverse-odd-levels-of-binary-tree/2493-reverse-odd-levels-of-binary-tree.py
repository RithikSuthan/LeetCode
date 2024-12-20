# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def inOrder(node1, node2, level):
            if node1 is None or node2 is None:
                return
            if(level % 2 != 0):
                node1.val, node2.val = node2.val, node1.val
            inOrder(node1.left, node2.right, level + 1)
            inOrder(node2.left, node1.right, level + 1)
            
        inOrder(root.left, root.right, 1)
        return root