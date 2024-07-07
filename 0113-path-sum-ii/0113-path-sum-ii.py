# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        ans=[]
        def inorder(root,ls,sum1):
            if root is None:
                return 
            ls.append(root.val)
            sum1+=root.val
            if sum1==targetSum and not root.left and not root.right:
                ans.append(ls[:])
            inorder(root.left,ls,sum1)
            inorder(root.right,ls,sum1)
            ls.pop()
        inorder(root,[],0)
        return ans
        