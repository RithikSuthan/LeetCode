# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def postOrder(self,root,target):
        if root is None:
            return None
        root.left=self.postOrder(root.left,target)
        root.right=self.postOrder(root.right,target)
        if root.val==target and root.left==None and root.right==None:
            return None
        return root
    def removeLeafNodes(self, root, target):
        return self.postOrder(root,target)

        