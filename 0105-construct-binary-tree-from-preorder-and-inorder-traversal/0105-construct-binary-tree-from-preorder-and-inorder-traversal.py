# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if len(preorder)==0 or len(inorder)==0:
            return
        root=TreeNode(preorder[0])
        ind=inorder.index(preorder[0])
        root.left=self.buildTree(preorder[1:ind+1],inorder[0:ind])
        root.right=self.buildTree(preorder[ind+1:],inorder[ind+1::])
        return root