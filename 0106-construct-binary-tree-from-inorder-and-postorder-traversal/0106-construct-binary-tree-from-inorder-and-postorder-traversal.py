# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        if len(inorder)==0 and len(postorder)==0:
            return 
        root=TreeNode(postorder[len(postorder)-1])
        ind=inorder.index(root.val)
        root.left=self.buildTree(inorder[0:ind],postorder[0:ind])
        root.right=self.buildTree(inorder[ind+1:],postorder[ind:len(postorder)-1])
        return root

        