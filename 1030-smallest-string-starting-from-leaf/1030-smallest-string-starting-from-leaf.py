# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        ans=[]
        def preorder(root,ls):
            nonlocal ans
            if root is None:
                return
            ls+=chr(root.val+97)
            if not root.left and not root.right:
               ans.append(ls[::-1])
            preorder(root.left,ls)
            preorder(root.right,ls)
            ls=ls[0:len(ls)-1:]
        preorder(root,"")
        ans.sort()
        # print(ans)
        return ans[0]