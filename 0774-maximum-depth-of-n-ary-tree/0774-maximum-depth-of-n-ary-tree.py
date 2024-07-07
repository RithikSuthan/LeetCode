"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        def height(root):
            if root is None:
                return 0
            max_height=0
            for i in root.children:
                max_height=max(max_height,height(i))
            return 1+max_height
        return height(root)
                