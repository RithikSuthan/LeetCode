# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        result=float("inf")
        if root is None:
            return 0
        def height(root):
            if root is None:
                return 0
            return 1+max(height(root.left),height(root.right))
        def print_current_level(root,level,ind):
            nonlocal result
            if root is None:
                return
            elif level==1:
                if not root.left and not root.right:
                    result=min(result,ind)
            else:
                print_current_level(root.left,level-1,ind)
                print_current_level(root.right,level-1,ind)
        h=height(root)
        for i in range(1,h+1):
            print_current_level(root,i,i)
            if result!=float("inf"):
                break
        # print(h)
        # print(result)
        return result