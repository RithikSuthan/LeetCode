# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        ans=[]
        def preorder(root,ls):
            nonlocal ans
            if root is None:
                return
            ls+=str(root.val)+"->"
            if not root.left and not root.right:
                ans.append(ls[0:len(ls)-2])
            preorder(root.left,ls)
            preorder(root.right,ls)
            # ls=ls[0:len(ls)-1]
        preorder(root,"")
        print(ans)
        return ans