# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def preorder(root,p,q):
            if root is None:
                return 
            # print(root.val," ",p.val," ",q.val)
            if (root.val >p.val and root.val >q.val):
                # print("FDes")
                return preorder(root.left,p,q)
            elif (root.val <p.val and root.val <q.val):
                return preorder(root.right,p,q)
            else:
                # print("elss")
                return root
        return preorder(root,p,q)