# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        ans=[]
        temp=to_delete[:]
        def preOrder(root,prev,temp):
            nonlocal ans
            if root is None:
                return
            if root.val in to_delete:
                to_delete.remove(root.val)
                if root.left and root.left.val not in to_delete:
                    ans.append(root.left)
                if root.right and root.right.val not in to_delete:
                    ans.append(root.right)
                if temp=="left":
                    prev.left=None
                elif temp=="right":
                    prev.right=None
            preOrder(root.left,root,"left")
            preOrder(root.right,root,"right") 
        preOrder(root,root,"")
        if root.val not in temp:
            ans.append(root)
        return ans