"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        ls=[]
        def traversal(root):
            if root is None:
                return
            for child in root.children:
                traversal(child)
            ls.append(root.val)
        traversal(root)
        return ls