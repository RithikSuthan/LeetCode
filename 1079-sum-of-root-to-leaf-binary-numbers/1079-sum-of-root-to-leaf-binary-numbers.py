# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        ls1=[]
        def path(root,ls):
            if root is None:
                return
            ls.append(str(root.val))
            path(root.left,ls)
            if not root.left and not root.right:
                ls1.append("0b"+"".join(ls[:]))
            path(root.right,ls)
            ls.pop()
        path(root,[])
        result=0
        # print(ls1)
        for i in ls1:
            result+=int(i,2)
        return result