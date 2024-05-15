# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def traversal(self,root,ls):
        if root==None:
            return
        root.left=self.traversal(root.left,ls)
        ls.append(root.val)
        root.right=self.traversal(root.right,ls)
        return ls
    def inorderTraversal(self, root):
        ls=[]
        ls=self.traversal(root,ls)
        return ls
