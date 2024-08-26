"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        ls=[]
        def traversal(root):
            if root is None:
                return
            ls.append(root.val)
            for child in root.children:
                traversal(child)
        traversal(root)
        return ls