# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        st=set()
        def inorder(root):
            if root is None:
                return
            inorder(root.left)
            st.add(root.val)
            inorder(root.right)
        inorder(root)
        st=sorted(st)
        if len(st)<=1:
            return -1
        return st[1]
